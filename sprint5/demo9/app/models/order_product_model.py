from dataclasses import dataclass
from sqlalchemy import Column, Integer, ForeignKey, Float

from app.configs.database import db

# from app.models.product_model import Product


@dataclass
class OrderProduct(db.Model):
    # register_id: int
    product_id: int
    order_id: int
    sale_value: float

    __tablename__ = "orders_products"

    register_id = Column(Integer, primary_key=True)
    sale_value = Column(Float, nullable=False)

    order_id = Column(Integer, ForeignKey("orders.id"))
    # products.product_id
    product_id = Column(Integer, ForeignKey("products.product_id"))
