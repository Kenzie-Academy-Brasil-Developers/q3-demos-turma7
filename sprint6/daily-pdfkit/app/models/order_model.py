from sqlalchemy import Column, ForeignKey, Integer
from app.configs.database import db


order_model = db.Table(
    "orders",
    Column("id", Integer, primary_key=True),
    Column("user_id", Integer, ForeignKey("users.id")),
    Column("product_id", Integer, ForeignKey("products.id")),
)
