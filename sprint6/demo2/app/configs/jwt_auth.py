from flask import Flask
from flask_jwt_extended import JWTManager
import os

# jwt = JWTManager()


def init_app(app: Flask):
    app.config["JWT_SECRET_KEY"] = os.getenv("SECRET")
    JWTManager(app)
    # jwt.init_app(app)
