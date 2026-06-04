def generate_schema(df_manager):

    schema = ""

    for table_name, df in df_manager.tables.items():

        schema += f"\n{table_name}\n"
        schema += "-" * len(table_name) + "\n"

        schema += "\n".join(df.columns)

        schema += "\n\n"

    return schema
