import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()   # 👈 REQUIRED

def get_llm():
    return ChatOpenAI(
        model="mistralai/mistral-medium",
        temperature=0,
        openai_api_key=os.getenv("OPENAI_API_KEY"),
        openai_api_base="https://openrouter.ai/api/v1"
    )
