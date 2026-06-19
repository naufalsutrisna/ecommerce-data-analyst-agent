from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

import os

load_dotenv()

BASE_CONFIG = {
    "api_key": os.getenv("OPENROUTER_API_KEY"),
    "base_url": os.getenv("OPENROUTER_BASE_URL"),
    "temperature": float(os.getenv("TEMPERATURE")),
    "max_tokens": int(os.getenv("MAX_TOKEN")),
}

small_llm = ChatOpenAI(
    model=os.getenv("OPENROUTER_SMALL_MODEL"),
    **BASE_CONFIG
)

large_llm = ChatOpenAI(
    model=os.getenv("OPENROUTER_LARGE_MODEL"),
    **BASE_CONFIG
)
