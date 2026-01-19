from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatOpenAI(
    model="mistralai/mistral-medium",
    temperature=0,
    openai_api_key=os.getenv("OPENAI_API_KEY"),
    openai_api_base="https://openrouter.ai/api/v1"
)

SCHEMA = """
Table: donations
Columns:
- donor_name (text)
- state (text)
- amount (number)
- donation_date (date)
"""

llm = ChatOpenAI(
    model="mistralai/mistral-medium",
    temperature=0,
    openai_api_key=os.getenv("OPENAI_API_KEY"),
    openai_api_base="https://openrouter.ai/api/v1",
    default_headers={
        "HTTP-Referer": "http://localhost:5000",
        "X-Title": "SQL Chat Assistant"
    }
)

def generate_sql(user_question: str) -> str:
    prompt = f"""
You are an expert MySQL assistant.

Database schema:
{SCHEMA}

Rules:
- Generate ONLY valid MySQL SQL
- Use LIKE for partial name matches
- Handle spelling mistakes gracefully
- Use YEAR(donation_date) when filtering by year
- NEVER hallucinate columns or tables

User question:
"{user_question}"

SQL:
"""
    response = llm.invoke(prompt)
    return response.content.strip()
