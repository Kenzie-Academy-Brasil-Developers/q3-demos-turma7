from flask import Flask
from . import database, migrate, email


def init_app(app: Flask) -> None:
    database.init_app(app)
    migrate.init_app(app)
    email.init_app(app)
