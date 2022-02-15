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

    # 1- Usando a model
    # customer_id = Column(Integer, ForeignKey(User.user_id))

    # 2- Utilizando string como referencia
    customer_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)

    # customer[0] -> lista
    # uselist=False -> Invés de ser uma lista de objetos da classe User, é somente um objeto
    customer = relationship("User", back_populates="orders", uselist=False)
