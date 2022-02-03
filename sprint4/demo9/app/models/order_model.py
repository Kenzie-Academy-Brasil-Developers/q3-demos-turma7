from . import DatabaseConnector
from psycopg2 import sql


class Order(DatabaseConnector):
    order_keys = ["order_id", "order_date", "customer_id"]
    table_name = "orders"

    def __init__(self, *args, **kwargs):
        self.order_id = kwargs["order_id"]
        self.order_date = kwargs["order_date"]
        self.customer_id = kwargs["customer_id"]

    @classmethod
    def select_order_by_id(cls, id: int, columns: list[str] = None):
        if not columns:
            columns = cls.order_keys

        cls.get_conn_cur()

        sql_table_name = sql.Identifier(cls.table_name)
        sql_id = sql.Literal(id)
        sql_columns = [sql.Identifier(column) for column in columns]

        if len(sql_columns) > 1:
            columns_join = sql.SQL(",").join(sql_columns)
        else:
            columns_join = sql_columns[0]

        query = sql.SQL(
            """
                SELECT
                    {sql_columns}
                FROM
                    {sql_table_name}
                JOIN
                    users u
                    ON u.user_id = {sql_table_name}.customer_id
                WHERE
                    {sql_table_name}.order_id = {sql_id};
            """
        ).format(sql_table_name=sql_table_name, sql_columns=columns_join, sql_id=sql_id)

        cls.cur.execute(query)

        order = cls.cur.fetchone()

        print("=" * 100)
        print(query.as_string(cls.cur))
        print("=" * 100)

        cls.commit_and_close()

        serialized_order = cls.serializer(order, columns)
        order_products = cls.get_order_products(id)

        serialized_order.update(order_products)

        return serialized_order

    @classmethod
    def select_all(cls):
        return super().select_all(cls.table_name)

    @classmethod
    def serializer(cls, data: tuple, keys: list["str"] = order_keys):
        return super().serializer(data, keys)

    @classmethod
    def get_order_products(cls, id: int):
        cls.get_conn_cur()

        query = """
            SELECT
                p.product_id, p."name", op.sale_value
            FROM
                orders o
            JOIN
                orders_products op
                ON o.order_id = op.order_id
            JOIN
                products p
                ON p.product_id = op.product_id
            WHERE
                o.order_id = %s;
        """

        cls.cur.execute(query, (id,))

        products = cls.cur.fetchall()

        if not products:
            return products

        desired_keys = ["product_id", "name", "sale_value"]
        serialized_products = [
            cls.serializer(product, desired_keys) for product in products
        ]

        cls.commit_and_close()

        products = {"products": serialized_products}

        return products
