# 🛒 E-commerce Data Analyst Agent

An AI-powered business analyst that allows users to ask natural language questions about the Olist Brazilian E-commerce dataset and receive data-driven insights.

---

## ✨ Features

### Natural Language Analytics

Ask questions in plain English:

> How many unique customers are there in each state?

> What are the top product categories by revenue?

> Which sellers generate the highest sales?

---

### Text-to-SQL Generation

The application uses an LLM to:

1. Understand the user's business question
2. Generate SQL queries automatically
3. Execute queries against in-memory datasets

Example:

```sql
SELECT
    customer_state,
    COUNT(DISTINCT customer_unique_id) AS unique_customers
FROM customers
GROUP BY customer_state;
```

---

### DuckDB Query Engine

Instead of requiring a database server, the project:

- Loads CSV datasets into Pandas DataFrames
- Registers DataFrames as SQL tables using DuckDB
- Executes generated SQL queries directly on in-memory data

---

### AI-Generated Business Insights

After executing SQL, the application automatically generates:

- Executive Summary
- Key Findings
- Business Implications

based on the query results.

---

### Interactive Chat Interface

Built with Streamlit.

Workflow:

```text
User Question
      ↓
LLM SQL Generator
      ↓
DuckDB Execution
      ↓
Query Result
      ↓
LLM Insight Generator
      ↓
Business Report
```

---

## 📊 Dataset

This project uses the Brazilian E-commerce dataset from Olist:

👉 https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce/

### Instructions:

* Download the dataset manually from Kaggle
* Extract all `.csv` files into the `data/` folder

Expected structure:

```bash
data/
├── olist_orders_dataset.csv
├── olist_customers_dataset.csv
├── olist_order_items_dataset.csv
├── olist_products_dataset.csv
├── olist_sellers_dataset.csv
└── ...
```

---

## 🚀 Running the Application

Start the Streamlit application:

```bash
python -m streamlit run app.py
```

Open:

```text
http://localhost:8501
```

---

## 🚀 Setup Instructions

### 1. Clone Repository

```bash
git clone https://github.com/naufalsutrisna/ecommerce-data-analyst-agent.git
cd ecommerce-data-analyst-agent
```

---

### 2. Create Virtual Environment

```bash
python -m venv .venv
```

---

### 3. Activate Virtual Environment

#### macOS / Linux

```bash
source .venv/bin/activate
```

#### Windows

```bash
.venv\Scripts\activate
```

---

### 4. Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

### 5. Configure Environment Variables

Create a `.env` file:

```env
OPENAI_API_KEY=your_api_key_here
```

---

### 6. Run Application

```bash
python -m streamlit run app.py
```

---

### 7. Deactivate Environment

```bash
deactivate
```

---
