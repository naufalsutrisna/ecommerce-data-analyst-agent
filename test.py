from services.dataframe_manager import DataFrameManager
from services.duckdb_manager import DuckDBManager
from services.schema_generator import generate_schema
from services.prompts import (
    BUSINESS_RULES_PROMPT,
    SQL_GENERATION_PROMPT,
    INSIGHT_GENERATION_PROMPT
)
from services.llm import llm

df_manager = DataFrameManager()

duckdb_manager = DuckDBManager(
    df_manager.tables
)

schema = generate_schema(df_manager)

question = """
How many unique customers are there in each state?
"""

formatted_prompt = SQL_GENERATION_PROMPT.format(
    business_rules=BUSINESS_RULES_PROMPT,
    schema=schema,
    question=question
)

print("=" * 50)
print(formatted_prompt)
print("=" * 50)

chain = SQL_GENERATION_PROMPT | llm

response = chain.invoke(
    {
        "business_rules": BUSINESS_RULES_PROMPT,
        "schema": schema,
        "question": question,
    }
)

print(response.content)

generated_sql = response.content

try:
    result_df = duckdb_manager.execute(
        response.content
    )

    print(result_df)
    
    insight_chain = INSIGHT_GENERATION_PROMPT | llm

    insight = insight_chain.invoke(
        {
            "question": question,
            "data": result_df.to_string(index=False)
        }
    )

    print(insight.content)

except Exception as e:
    print(f"SQL Execution Error: {e}")
