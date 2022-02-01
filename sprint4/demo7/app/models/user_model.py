from app.models import DatabaseConnector
from psycopg2 import sql

# from app.models import conn


class User(DatabaseConnector):
    user_keys = ["id", "email", "birthdate", "children", "married", "account_balance"]

    def __init__(self, *args, **kwargs):
        self.email = kwargs["email"]
        self.birthdate = kwargs["birthdate"]
        self.children = kwargs["children"]
        self.married = kwargs["married"]
        self.account_balance = kwargs["account_balance"]

    @classmethod
    def read_users(cls):
        cls.get_conn_cur()

        query = "SELECT * FROM users;"

        cls.cur.execute(query)

        # cur.fetch_one()

        # Retorno é uma lista de tuplas
        users = cls.cur.fetchall()
        # print(users)

        cls.commit_and_close()

        return users

    @staticmethod
    def serialize_user(data, keys=user_keys):
        if type(data) is tuple:
            return dict(zip(keys, data))
        if type(data) is list:
            return [dict(zip(keys, user)) for user in data]

        # return "tipo inválido"

    @classmethod
    def update_user(cls, user_id, payload):
        cls.get_conn_cur()

        columns = [sql.Identifier(key) for key in payload.keys()]
        values = [sql.Literal(value) for value in payload.values()]

        # print(type(columns[0]))
        # print(type(values[0]))

        query = sql.SQL(
            """
                UPDATE
                    users
                SET
                    ({columns}) = ROW({values})
                WHERE
                    id={id}
                RETURNING *
            """
        ).format(
            id=sql.Literal(user_id),
            columns=sql.SQL(",").join(columns),
            values=sql.SQL(",").join(values),
        )

        # print("*" * 100)
        # print(query.as_string(cls.cur))
        # print("*" * 100)

        cls.cur.execute(query)
        updated_user = cls.cur.fetchone()

        cls.commit_and_close()

        return updated_user

    def create_user(self):
        self.get_conn_cur()

        query = """
            INSERT INTO
                users (email, birthdate, children, married, account_balance)
            VALUES
                (%s, %s, %s, %s, %s)
            RETURNING *
        """

        query_values = list(self.__dict__.values())

        self.cur.execute(query, query_values)

        print(self.__dict__)

        # Retorno é uma unica tupla
        inserted_user = self.cur.fetchone()

        self.commit_and_close()

        return inserted_user

    @classmethod
    def read_users_by_email(cls, email):
        cls.get_conn_cur()

        # FORMA ERRADA
        query = f"SELECT * FROM users WHERE email LIKE '%{email}%';"

        print("*" * 100)
        print(query)
        print("*" * 100)

        cls.cur.execute(query)

        # Retorno é uma lista de tuplas
        users = cls.cur.fetchall()
        # print(users)

        cls.commit_and_close()

        return users

    
