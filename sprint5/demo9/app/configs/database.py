from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import os

db = SQLAlchemy()

# db.create_all()


def init_app(app: Flask):
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DB_URI")

    db.init_app(app)
    app.db = db

    # TODO: Melhorar ciclo de imports via models/__init__.py
    from app.models.user_model import User
    from app.models.order_model import Order
    from app.models.invoice_model import Invoice
    from app.models.product_model import Product
    from app.models.order_product_model import OrderProduct
