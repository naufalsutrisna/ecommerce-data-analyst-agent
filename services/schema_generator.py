def generate_schema(df_manager):

    schema = []

    for table_name, df in df_manager.tables.items():

        columns = []

        for col, dtype in df.dtypes.items():
            columns.append(
                f"{col} ({dtype})"
            )

        schema.append(f"""
        Table: {table_name}

        Columns:
        {', '.join(columns)}
        """)

    return "\n".join(schema)
