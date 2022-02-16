from dataclasses import dataclass
from sqlalchemy import Column, Integer, String, Text, Float

from app.configs.database import db


@dataclass
class Product(db.Model):
    product_id: int
    name: str
    description: str
    price: float

    __tablename__ = "products"

    product_id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    description = Column(Text, default="No Description")
    price = Column(Float, nullable=False)
