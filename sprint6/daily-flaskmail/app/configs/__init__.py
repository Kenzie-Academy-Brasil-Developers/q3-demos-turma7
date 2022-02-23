from flask import Flask
from . import email


def init_apps(app: Flask) -> None:
    email.init_app(app)
