import os
import json
import re
import requests
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import matplotlib.pyplot as plt
from flask import Flask, request, jsonify, render_template
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
from urllib.parse import quote_plus
import base64
from io import BytesIO

# =========================
# ENV + APP
# =========================
load_dotenv()
app = Flask(__name__)

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
if not OPENROUTER_API_KEY:
    raise RuntimeError("❌ OPENROUTER_API_KEY not set")

print("✅ OpenRouter key loaded")

# =========================
# DATABASE (FIXED)
# =========================
DB_USER = "root"
DB_PASS = quote_plus("Cosmos@152209")  # IMPORTANT
DB_HOST = "localhost"
DB_NAME = "Donation_db"

engine = create_engine(
    f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}",
    pool_pre_ping=True
)

# =========================
# OPENROUTER CALL
# =========================
def call_llm(prompt: str) -> str:
    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json",
            "HTTP-Referer": "http://localhost:5000",
            "X-Title": "AI SQL Chat Assistant"
        },
        json={
            "model": "openai/gpt-3.5-turbo",
            "messages": [
                {"role": "user", "content": prompt}
            ],
            "temperature": 0
        },
        timeout=30
    )

    if response.status_code != 200:
        print("❌ ERROR:", response.text)
        raise RuntimeError(response.text)

    return response.json()["choices"][0]["message"]["content"]

# =========================
# PROMPTS (FIXED COLUMN NAMES)
# =========================
SQL_PROMPT = """
You are an expert MySQL assistant.

Table name: donations

IMPORTANT: Use EXACT column names below (case-insensitive is OK):

- `Name of Donar`
- `Amount of Donation`
- `Receipt Date`
- `State`
- `City`
- `Mode Of Payment`

Rules:
- Use ONLY MySQL
- Use LIKE for donor names (partial match)
- Use SUM / COUNT / GROUP BY when required
- Handle spelling/case variations in names
- Output ONLY SQL
- End the query with a semicolon
- DO NOT explain anything

User question:
{question}

SQL:
"""

SUMMARY_PROMPT = """
Explain the result clearly for a non-technical user.

Question: {question}
SQL used: {sql}
Result data: {result}

Answer:
"""

ANALYTICAL_SUMMARY_PROMPT = """
You are analyzing donation data. Provide a comprehensive analytical summary.

Question: {question}
SQL used: {sql}
Result data: {result}

Provide insights including:
- Key findings and patterns
- Totals, averages, or percentages where relevant
- Top performers (states, donors, etc.)
- Notable trends or observations
- Comparisons between different groups

Keep it clear and actionable for decision-makers.

Answer:
"""

# =========================
# CHART DETECTION & GENERATION
# =========================
def needs_chart(question: str) -> tuple:
    """Check if query needs a chart and return chart type"""
    question_lower = question.lower()

    if "histogram" in question_lower:
        return True, "histogram"

    chart_keywords = {
        'pie': ['pie chart', 'pie graph', 'pie diagram'],
        'bar': ['bar chart', 'bar graph', 'bar diagram'],
        'line': ['line chart', 'line graph', 'trend', 'over time'],
        'scatter': ['scatter', 'scatter plot', 'correlation']
    }

    for chart_type, keywords in chart_keywords.items():
        if any(keyword in question_lower for keyword in keywords):
            return True, chart_type

    return False, None

def generate_chart(df: pd.DataFrame, chart_type: str, question: str):
    """Generate Plotly chart or Matplotlib histogram"""
    if df.empty or len(df.columns) < 1:
        return None, None

    try:
        cols = df.columns.tolist()

        amount_col = None
        for col in cols:
            if 'amount' in col.lower() or 'donation' in col.lower():
                amount_col = col
                break

        if not amount_col:
            amount_col = cols[-1]

        cat_col = cols[0]

        # ---------- HISTOGRAM (MATPLOTLIB) ----------
        if chart_type == "histogram":
            plt.figure()
            plt.hist(df[amount_col], bins=10)
            plt.title("Donation Amount Distribution")
            plt.xlabel("Amount")
            plt.ylabel("Frequency")

            buffer = BytesIO()
            plt.savefig(buffer, format="png")
            plt.close()
            buffer.seek(0)

            image_base64 = base64.b64encode(buffer.read()).decode("utf-8")
            return None, image_base64

        # ---------- PLOTLY CHARTS ----------
        if chart_type == 'pie':
            fig = px.pie(
                df,
                names=cat_col,
                values=amount_col,
                title=f"Distribution by {cat_col}",
                color_discrete_sequence=px.colors.sequential.Purples_r
            )
            fig.update_traces(textposition='inside', textinfo='percent+label')

        elif chart_type == 'bar':
            fig = px.bar(
                df,
                x=cat_col,
                y=amount_col,
                title=f"{amount_col} by {cat_col}",
                color=amount_col,
                color_continuous_scale='Purples'
            )
            fig.update_layout(showlegend=False)

        elif chart_type == 'line':
            fig = px.line(
                df,
                x=cat_col,
                y=amount_col,
                title=f"{amount_col} Trend",
                markers=True
            )

        else:  # scatter
            x_col = cols[0]
            y_col = cols[1] if len(cols) > 1 else cols[0]
            fig = px.scatter(
                df,
                x=x_col,
                y=y_col,
                title=f"{y_col} vs {x_col}",
                color=y_col if y_col != x_col else None,
                color_continuous_scale='Purples'
            )

        fig.update_layout(
            template='plotly_white',
            font=dict(family="Segoe UI, sans-serif"),
            title_font_size=18,
            title_font_color='#8e44ad',
            height=450,
            margin=dict(l=40, r=40, t=60, b=40)
        )

        return fig.to_html(include_plotlyjs='cdn', div_id='chart'), None

    except Exception as e:
        print(f"❌ Chart generation error: {e}")
        return None, None

# =========================
# LOGIC
# =========================
def is_analytical_query(question: str) -> bool:
    keywords = [
        'analyse', 'analyze', 'analysis', 'summarize', 'summarise',
        'summary', 'history', 'multiple', 'compare', 'comparison',
        'breakdown', 'distribution', 'pattern', 'trend', 'by state',
        'by city', 'by mode', 'group', 'all donations', 'top donors'
    ]
    return any(keyword in question.lower() for keyword in keywords)

def generate_sql(question: str) -> str:
    prompt = SQL_PROMPT.format(question=question)
    sql_text = call_llm(prompt)

    match = re.search(r"(SELECT[\s\S]*?;)", sql_text, re.I)
    if not match:
        raise ValueError(f"Invalid SQL generated:\n{sql_text}")

    return match.group(1)

def run_query(sql: str) -> pd.DataFrame:
    with engine.connect() as conn:
        return pd.read_sql(text(sql), conn)

def summarize(question: str, sql: str, df: pd.DataFrame, is_analytical: bool = False) -> str:
    if df.empty:
        return "No donation records were found matching your question."

    if is_analytical:
        prompt = ANALYTICAL_SUMMARY_PROMPT.format(
            question=question,
            sql=sql,
            result=json.dumps(df.to_dict(orient="records"))
        )
    else:
        prompt = SUMMARY_PROMPT.format(
            question=question,
            sql=sql,
            result=json.dumps(df.to_dict(orient="records"))
        )

    return call_llm(prompt)

# =========================
# ROUTES
# =========================
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    try:
        data = request.get_json(force=True)
        question = data.get("question", "").strip()

        if not question:
            return jsonify({"error": "Question cannot be empty"}), 400

        is_analytical = is_analytical_query(question)
        chart_needed, chart_type = needs_chart(question)

        sql = generate_sql(question)
        df = run_query(sql)
        answer = summarize(question, sql, df, is_analytical or chart_needed)

        chart_html = None
        chart_image = None

        if chart_needed and not df.empty:
            chart_html, chart_image = generate_chart(df, chart_type, question)

        return jsonify({
            "question": question,
            "sql": sql,
            "answer": answer,
            "rows": df.to_dict(orient="records"),
            "show_table": is_analytical,
            "chart_html": chart_html,
            "chart_image": chart_image
        })

    except Exception as e:
        print("❌ ERROR:", e)
        return jsonify({"error": str(e)}), 500

# =========================
# START
# =========================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

