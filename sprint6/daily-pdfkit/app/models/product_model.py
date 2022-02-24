from dataclasses import dataclass
from app.configs.database import db
from sqlalchemy import Column, Integer, Numeric, String


@dataclass
class ProductModel(db.Model):
    __tablename__ = "products"

    id: int = Column(Integer, primary_key=True)
    name: str = Column(String)
    price: bool = Column(Numeric)
