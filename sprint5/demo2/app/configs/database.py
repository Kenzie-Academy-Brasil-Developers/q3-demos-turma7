from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import os

# Desing Pattern - Singleton
db = SQLAlchemy()

# print(f"{__name__} DB -> {id(db)}")


def init_app(app: Flask):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DB_URI")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    # Criar atributo pós objeto criado
    # app.batata = "Batata"
    # print(app.batata)

    app.db = db

    from app.models.call_record_model import CallRecord

    # db.create_all(app=app)
    # db.drop_all(app=app)
