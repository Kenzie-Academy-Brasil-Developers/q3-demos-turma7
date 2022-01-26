from app.models import conn


class User:
    def __init__(self, *args, **kwargs):
        self.email = kwargs["email"]
        self.birthdate = kwargs["birthdate"]
        self.children = kwargs["children"]
        self.married = kwargs["married"]
        self.account_balance = kwargs["account_balance"]

    @staticmethod
    def read_users():
        cur = conn.cursor()

        query = "SELECT * FROM users;"

        cur.execute(query)

        # cur.fetch_one()
        users = cur.fetchall()
        print(users)

        cur.close()
        conn.close()

        return users
