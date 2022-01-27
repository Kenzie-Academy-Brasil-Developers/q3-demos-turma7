from app.models import DatabaseConnector

# from app.models import conn


class User(DatabaseConnector):
    def __init__(self, *args, **kwargs):
        self.email = kwargs["email"]
        self.birthdate = kwargs["birthdate"]
        self.children = kwargs["children"]
        self.married = kwargs["married"]
        self.account_balance = kwargs["account_balance"]

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
