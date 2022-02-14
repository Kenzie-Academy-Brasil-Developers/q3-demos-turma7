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

    from app.models.user_model import User
    from app.models.order_model import Order
