BUSINESS_RULES_PROMPT = """
    Use customer_unique_id when counting customers.

    Do not use customer_id when counting customers.
"""

SQL_GENERATION_PROMPT = """
    You are a senior data analyst.

    Business Rules:
    {business_rules}

    Schema:
    {schema}

    Question:
    {question}

    Rules:
    - Return SQL only.
    - Do not explain your answer.
    - Do not use markdown.
    - Do not wrap the SQL in ```sql blocks.
"""
