from sqlalchemy import Column, Integer, String, Date, Boolean, Float
from dataclasses import dataclass
from sqlalchemy.orm import relationship
from app.configs.database import db


@dataclass
class User(db.Model):
    user_id: int
    email: str
    birthdate: str
    children: int
    married: bool
    account_balance: float
    orders: str

    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True)
    email = Column(String(64), unique=True, nullable=False)
    birthdate = Column(Date, nullable=False)
    children = Column(Integer, nullable=False)
    married = Column(Boolean, nullable=False)
    account_balance = Column(Float(2))

    orders = relationship("Order", back_populates="customer", uselist=True)
