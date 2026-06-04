from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

import os

load_dotenv()

llm = ChatOpenAI(
    model=os.getenv("OPENROUTER_MODEL"),
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url=os.getenv("OPENROUTER_BASE_URL"),
    max_tokens=int(os.getenv("MAX_TOKEN")),
    temperature=0
)
