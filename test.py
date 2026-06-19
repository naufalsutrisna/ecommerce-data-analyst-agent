from services.dataframe_manager import DataFrameManager
from services.duckdb_manager import DuckDBManager
from services.schema_generator import generate_schema
from services.prompts import (
    QUESTION_CLASSIFIER_PROMPT,
    OUT_OF_SCOPE_RESPONSE,
    BUSINESS_RULES_PROMPT,
    SQL_GENERATION_PROMPT,
    INSIGHT_GENERATION_PROMPT
)
from services.llm import small_llm, large_llm

df_manager = DataFrameManager()

duckdb_manager = DuckDBManager(
    df_manager.tables
)

schema = generate_schema(df_manager)

question = """
How many unique customers are there in each state?
"""

# Classifier
classifier_chain = QUESTION_CLASSIFIER_PROMPT | small_llm

classification = (
    classifier_chain.invoke(
        {
            "question": question
        }
    )
    .content
    .strip()
)

print(f"Classification: {classification}")

if classification != "ANALYTICS":
    print(OUT_OF_SCOPE_RESPONSE)

else:
    formatted_prompt = SQL_GENERATION_PROMPT.format(
        business_rules=BUSINESS_RULES_PROMPT,
        schema=schema,
        question=question
    )

    print("=" * 50)
    print(formatted_prompt)
    print("=" * 50)

    sql_chain = SQL_GENERATION_PROMPT | large_llm

    generated_sql = sql_chain.invoke(
        {
            "business_rules": BUSINESS_RULES_PROMPT,
            "schema": schema,
            "question": question,
        }
    )

    print(generated_sql.content)

    try:
        result_df = duckdb_manager.execute(
            generated_sql.content
        )

        print(result_df)
        
        insight_chain = INSIGHT_GENERATION_PROMPT | large_llm

        insight = insight_chain.invoke(
            {
                "question": question,
                "data": result_df.to_string(index=False)
            }
        )

        print(insight.content)

    except Exception as e:
        print(f"SQL Execution Error: {e}")
