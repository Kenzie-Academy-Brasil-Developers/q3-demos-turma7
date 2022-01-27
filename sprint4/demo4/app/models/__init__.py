from os import getenv
import psycopg2

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
