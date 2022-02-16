from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from dataclasses import dataclass
from app.configs.database import db

# from app.models.user_model import User


@dataclass
class Order(db.Model):
    id: int
    order_date: str
    # customer_id: int

    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)
    order_date = Column(DateTime, nullable=False)

    customer_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)

    customer = relationship("User", back_populates="orders", uselist=False)

    # relationships nao precisam ser bilaterais
    products = relationship("Product", secondary="orders_products")
