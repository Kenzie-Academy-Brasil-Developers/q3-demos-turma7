from os import getenv
import psycopg2
from psycopg2 import sql

# 0. Decorator (bem mais complexo, overkill)
# 1. Gerenciador de contexto with
# 2. Criar uma funcao que retornasse conn
# 3. Utilizar herança e POO para conexao


configs = {
    "host": getenv("DB_HOST"),
    "database": getenv("DB_NAME"),
    "user": getenv("DB_USER"),
    "password": getenv("DB_PASSWORD"),
}

# conn = psycopg2.connect(**configs)


class DatabaseConnector:
    @classmethod
    def get_conn_cur(cls):
        cls.conn = psycopg2.connect(**configs)
        cls.cur = cls.conn.cursor()

    @classmethod
    def commit_and_close(cls):
        cls.conn.commit()
        cls.cur.close()
        cls.conn.close()

    @classmethod
    def insert_into(cls, payload: dict, table_name: str):
        cls.get_conn_cur()

        sql_table_name = sql.Identifier(table_name)
        columns = [sql.Identifier(key) for key in payload.keys()]
        values = [sql.Literal(value) for value in payload.values()]

        query = sql.SQL(
            """
                INSERT INTO
                    {sql_table_name} ({columns})
                VALUES
                    ({values})
                RETURNING *
            """
        ).format(
            sql_table_name=sql_table_name,
            columns=sql.SQL(",").join(columns),
            values=sql.SQL(",").join(values),
        )

        cls.cur.execute(query)

        inserted_data = cls.cur.fetchone()

        print("=" * 100)
        print(query.as_string(cls.cur))
        print("=" * 100)

        cls.commit_and_close()

        return inserted_data

    @classmethod
    def get_column_names(cls, table_name: str):
        cls.get_conn_cur()

        query = sql.SQL(
            """
            SELECT
                column_name
            FROM
                information_schema.COLUMNS
            WHERE table_name = {table_name}
            ORDER BY ordinal_position;
            """
        ).format(table_name=sql.Literal(table_name))

        cls.cur.execute(query)

        column_names = cls.cur.fetchall()

        # print("=" * 100)
        # print(column_names)
        # print("=" * 100)

        cls.commit_and_close()

        return [row[0] for row in column_names]

    @classmethod
    def select_all(cls, table_name: str):
        cls.get_conn_cur()

        # Nome de coluna SQL "table_name"
        # SELECT * FROM 'table_name';
        sql_table_name = sql.Identifier(table_name)

        query = sql.SQL(
            """
                SELECT * FROM {sql_table_name};
            """
        ).format(sql_table_name=sql_table_name)

        cls.cur.execute(query)

        print("=" * 100)
        print(query.as_string(cls.cur))
        print("=" * 100)

        result = cls.cur.fetchall()

        cls.commit_and_close()

        return result

    @classmethod
    def serializer(cls, data: tuple, keys: list[str]):
        return dict(zip(keys, data))
