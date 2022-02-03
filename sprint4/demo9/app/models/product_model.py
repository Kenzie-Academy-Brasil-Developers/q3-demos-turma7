from app.models import DatabaseConnector


class Product(DatabaseConnector):
    table_name = "products"
    product_columns = DatabaseConnector.get_column_names(table_name)

    def __init__(self, *args, **kwargs):
        self.name = kwargs["name"]
        self.price = kwargs["price"]

    def insert_into(self):
        return super().insert_into(self.__dict__, self.table_name)

    @classmethod
    def select_all(cls, table_name: str = table_name):
        return super().select_all(table_name)

    @classmethod
    def serializer(cls, data: tuple, keys: list[str] = product_columns):
        return super().serializer(data, keys)
