import streamlit as st

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
from services.llm import (
    small_llm,
    large_llm
)

@st.cache_resource
def initialize():

    df_manager = DataFrameManager()

    duckdb_manager = DuckDBManager(
        df_manager.tables
    )

    schema = generate_schema(df_manager)

    return duckdb_manager, schema


duckdb_manager, schema = initialize()

st.title("🛒 Ecommerce Data Analyst Agent")
st.caption("Ask business questions about the Olist dataset")

if "messages" not in st.session_state:
    st.session_state.messages = []
    
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        
question = st.chat_input(
    "Ask a question..."
)

if question:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):

        with st.spinner("Analyzing..."):

            try:
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

                if classification != "ANALYTICS":

                    st.warning(
                        OUT_OF_SCOPE_RESPONSE
                    )

                    st.session_state.messages.append(
                        {
                            "role": "assistant",
                            "content": OUT_OF_SCOPE_RESPONSE
                        }
                    )

                else:

                    # SQL Generation
                    sql_chain = SQL_GENERATION_PROMPT | large_llm

                    sql_response = sql_chain.invoke(
                        {
                            "business_rules": BUSINESS_RULES_PROMPT,
                            "schema": schema,
                            "question": question,
                        }
                    )

                    generated_sql = sql_response.content

                    # Execute SQL
                    result_df = duckdb_manager.execute(
                        generated_sql
                    )

                    # Generate Insight
                    insight_chain = INSIGHT_GENERATION_PROMPT | large_llm

                    insight = insight_chain.invoke(
                        {
                            "question": question,
                            "data": result_df.to_string(
                                index=False
                            )
                        }
                    )

                    st.markdown(insight.content)

                    # with st.expander(
                    #     "Generated SQL"
                    # ):
                    #     st.code(
                    #         generated_sql,
                    #         language="sql"
                    #     )

                    # with st.expander(
                    #     "Query Result"
                    # ):
                    #     st.dataframe(
                    #         result_df,
                    #         use_container_width=True
                    #     )

                    st.session_state.messages.append(
                        {
                            "role": "assistant",
                            "content": insight.content
                        }
                    )

            except Exception as e:

                st.error(
                    f"Error: {str(e)}"
                )
