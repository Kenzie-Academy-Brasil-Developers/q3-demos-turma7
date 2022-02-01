from . import DatabaseConnector


class Order(DatabaseConnector):
    order_keys = ["order_id", "order_date", "customer_id"]
    table_name = "orders"

    def __init__(self, *args, **kwargs):
        self.order_id = kwargs["order_id"]
        self.order_date = kwargs["order_date"]
        self.customer_id = kwargs["customer_id"]

    @classmethod
    def select_all(cls):
        return super().select_all(cls.table_name)

    @classmethod
    def serializer(cls, data: tuple):
        return super().serializer(data, cls.order_keys)
