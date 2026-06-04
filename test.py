from services.dataframe_manager import DataFrameManager
from services.schema_generator import generate_schema
from services.prompts import (
    BUSINESS_RULES_PROMPT,
    SQL_GENERATION_PROMPT
)
from services.llm import llm

df_manager = DataFrameManager()

schema = generate_schema(df_manager)

question = """
How many unique customers are there in each state?
"""

prompt = SQL_GENERATION_PROMPT.format(
    business_rules=BUSINESS_RULES_PROMPT,
    schema=schema,
    question=question
)

print("=" * 50)
print(prompt)
print("=" * 50)

response = llm.invoke(prompt)

print(response.content)
