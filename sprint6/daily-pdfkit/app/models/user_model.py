from dataclasses import dataclass

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.configs.database import db
from app.models.product_model import ProductModel


@dataclass
class UserModel(db.Model):
    __tablename__ = "users"

    id: str = Column(Integer, primary_key=True)
    name: str = Column(String)
    email: str = Column(String)


    products: list[ProductModel] = relationship(
        "ProductModel", secondary="orders", backref="users"
    )
