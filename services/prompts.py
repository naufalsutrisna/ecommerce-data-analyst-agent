from langchain_core.prompts import PromptTemplate

QUESTION_CLASSIFIER_PROMPT = PromptTemplate.from_template("""
    You are a classifier for an Ecommerce Business Analytics Assistant.

    Your job is to determine whether a user's question requires analysis of the ecommerce dataset.

    Classify the question into exactly one category:

    ANALYTICS
    - Revenue analysis
    - Customer analysis
    - Product analysis
    - Seller analysis
    - Order analysis
    - Payment analysis
    - Delivery analysis
    - Business performance analysis
    - Trends and KPIs

    OUT_OF_SCOPE
    - General programming questions
    - SQL tutorials
    - Python tutorials
    - Math questions
    - General knowledge
    - Jokes
    - Creative writing
    - Questions unrelated to the ecommerce dataset

    Question:
    {question}

    Return only:

    ANALYTICS

    or

    OUT_OF_SCOPE
""")

OUT_OF_SCOPE_RESPONSE = """
    I am an Ecommerce Business Analytics Assistant.

    I can help answer questions related to:

    - Revenue
    - Orders
    - Customers
    - Products
    - Sellers
    - Payments
    - Delivery performance
    - Business KPIs

    Please ask a question related to the ecommerce dataset.
"""

BUSINESS_RULES_PROMPT = """
    Use customer_unique_id when counting customers.

    Do not use customer_id when counting customers.
"""

SQL_GENERATION_PROMPT = PromptTemplate.from_template("""
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
""")

INSIGHT_GENERATION_PROMPT = PromptTemplate.from_template("""
    You are a Senior Business Analyst.

    User Question:
    {question}

    SQL Result:
    {data}

    Generate:
    1. Executive Summary
    2. Key Findings
    3. Business Implications

    Only use information explicitly present in the data.

    Do not invent metrics.

    Do not make assumptions about:
    - acquisition cost
    - marketing effectiveness
    - profitability
    - customer satisfaction
    - logistics performance

    If evidence is unavailable, state that additional analysis is required.
""")
