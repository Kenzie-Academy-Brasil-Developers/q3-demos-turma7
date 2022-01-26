from flask import Flask, Blueprint
from app.controllers import user_controller

bp = Blueprint("users", __name__, url_prefix="/api")


# def user_route(app: Flask):
#     @bp.get("/users")
#     def retrieve():
#         return user_controller.get_users()


# @bp.get("/users")
# def retrieve():
#     return user_controller.get_users()


# Closures and Decorators
bp.get("/users")(user_controller.get_users)
