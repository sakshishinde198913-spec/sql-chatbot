from langchain_openai import ChatOpenAI
import os

llm = ChatOpenAI(
    model="mistralai/mistral-medium",
    temperature=0.2,
    openai_api_key=os.getenv("OPENAI_API_KEY"),
    openai_api_base="https://openrouter.ai/api/v1"
)

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

def summarize(question, sql, result):
    prompt = f"""
User question:
{question}

SQL used:
{sql}

SQL result:
{result}

Explain the answer clearly in natural language.
If the result is empty, explain politely.
"""
    return llm.invoke(prompt).content
