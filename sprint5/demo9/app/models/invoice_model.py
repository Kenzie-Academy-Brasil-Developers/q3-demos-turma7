from sqlalchemy import Column, Integer, DateTime, ForeignKey, String
from sqlalchemy.orm import relationship, backref
from datetime import datetime as dt

# pandas pd, numpy np
from dataclasses import dataclass

from app.configs.database import db


@dataclass
class Invoice(db.Model):
    invoice_id: int
    invoice_number: str
    release_time: str
    order_id: int

    __tablename__ = "invoices"
    # autoincrement
    # uuid
    invoice_id = Column(Integer, primary_key=True)
    invoice_number = Column(String(63), unique=True)
    release_time = Column(DateTime, default=dt.now())

    order_id = Column(Integer, ForeignKey("orders.id"), unique=True)

    # backref
    order = relationship("Order", backref=backref("invoice", uselist=False))
