import duckdb

class DuckDBManager:

    def __init__(self, tables: dict):

        self.conn = duckdb.connect()

        for table_name, df in tables.items():
            self.conn.register(table_name, df)

    def execute(self, sql: str):

        sql_clean = sql.strip().lower()

        if not sql_clean.startswith("select"):
            raise ValueError(
                "Only SELECT queries are allowed."
            )

        return self.conn.execute(sql).df()
