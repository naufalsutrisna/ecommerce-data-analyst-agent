# 🛒 E-commerce Data Analyst Agent

An AI-powered business analytics chatbot that enables users to explore the Olist Brazilian E-commerce dataset using natural language.

The application automatically converts business questions into SQL, executes queries using DuckDB, and generates executive-level business insights.

---

# ✨ Features

## Natural Language Business Analytics

Ask business questions in plain English:

> How many unique customers are there in each state?

> What are the top product categories by revenue?

> Which sellers generate the highest sales?

> What payment methods contribute the most revenue?

---

## Business Analytics Scope Validation

The chatbot is restricted to business analytics questions.

Questions unrelated to the ecommerce dataset are automatically rejected to prevent hallucinations and misuse.

Examples:

✅ Top 10 product categories by revenue

✅ Revenue by state

❌ How do SQL JOINs work?

❌ Write a Python function

---

## AI-Powered Text-to-SQL

The application uses Large Language Models (LLMs) to:

1. Understand business questions
2. Generate SQL queries
3. Validate business rules
4. Execute analytics queries

Example:

```sql
SELECT
    customer_state,
    COUNT(DISTINCT customer_unique_id) AS unique_customers
FROM customers_df
GROUP BY customer_state;
```

---

## DuckDB Query Engine

The project does not require a dedicated database server.

Workflow:

* Load CSV files into Pandas DataFrames
* Register DataFrames as DuckDB tables
* Execute generated SQL directly on in-memory datasets

Benefits:

* Lightweight
* Fast
* Easy local deployment
* No database setup required

---

## AI-Generated Business Insights

After query execution, the application automatically generates:

* Executive Summary
* Key Findings
* Business Implications

using an LLM-based business analyst agent.

---

## Interactive Chat Interface

Built using Streamlit.

Workflow:

```text
User Question
      ↓
Question Classifier
      ↓
SQL Generator
      ↓
DuckDB Execution
      ↓
Query Result
      ↓
Insight Generator
      ↓
Business Report
```

---

## Data Quality & Preprocessing

The application automatically performs preprocessing before analysis:

* Remove invalid delivered orders
* Handle missing product categories
* Create data quality indicators
* Flag products with missing catalog information
* Flag products with missing dimensions

This ensures more reliable business insights.

---

# 🏗️ Architecture

```text
Streamlit UI
      ↓
Question Classifier
      ↓
SQL Generation Agent
      ↓
DuckDB Query Engine
      ↓
Insight Generation Agent
      ↓
Business Report
```

Technologies:

* Python
* Streamlit
* Pandas
* DuckDB
* LangChain
* OpenRouter
* GPT-OSS Models

---

# 📊 Dataset

This project uses the Brazilian E-commerce dataset from Olist.

Dataset:

https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce

## Setup Dataset

Download the dataset manually from Kaggle.

Extract all CSV files into:

```text
data/
├── olist_orders_dataset.csv
├── olist_customers_dataset.csv
├── olist_order_items_dataset.csv
├── olist_products_dataset.csv
├── olist_sellers_dataset.csv
└── ...
```

---

# 🚀 Local Setup

## 1. Clone Repository

```bash
git clone https://github.com/naufalsutrisna/ecommerce-data-analyst-agent.git

cd ecommerce-data-analyst-agent
```

---

## 2. Create Virtual Environment

```bash
python -m venv .venv
```

---

## 3. Activate Environment

### macOS / Linux

```bash
source .venv/bin/activate
```

### Windows

```bash
.venv\Scripts\activate
```

---

## 4. Install Dependencies

```bash
pip install --upgrade pip

pip install -r requirements.txt
```

---

## 5. Configure Environment Variables

Create a `.env` file:

```env
OPENROUTER_API_KEY=

OPENROUTER_BASE_URL=https://openrouter.ai/api/v1

OPENROUTER_SMALL_MODEL=openai/gpt-oss-20b:free
OPENROUTER_LARGE_MODEL=openai/gpt-oss-120b:free

TEMPERATURE=0
MAX_TOKEN=2000

MAX_INSIGHT_ROWS=50
```

---

## 6. Run Application

```bash
streamlit run app.py
```

Open:

```text
http://localhost:8501
```

---

# 🐳 Docker

Build image:

```bash
docker build -t ecommerce-data-analyst-agent .
```

Run container:

```bash
docker run \
-p 8501:8501 \
--env-file .env \
ecommerce-data-analyst-agent
```

Open:

```text
http://localhost:8501
```

---

# 📁 Project Structure

```text
ecommerce-data-analyst-agent/
│
├── app.py
├── config.py
├── requirements.txt
├── Dockerfile
│
├── data/
│
├── prompts/
│
├── services/
│   ├── dataframe_manager.py
│   ├── duckdb_manager.py
│   ├── schema_generator.py
│   ├── llm.py
│   └── prompts.py
│
└── tests/
```
