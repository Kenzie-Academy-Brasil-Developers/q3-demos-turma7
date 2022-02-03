from flask import Flask, Blueprint
from app.controllers import user_controller

bp = Blueprint("users", __name__, url_prefix="/users")


# def user_route(app: Flask):
#     @bp.get("/users")
#     def retrieve():
#         return user_controller.get_users()


# @bp.get("/users")
# def retrieve():
#     return user_controller.get_users()


# Closures and Decorators
bp.get("")(user_controller.get_users)
bp.post("")(user_controller.create_user)
bp.patch("/<int:user_id>")(user_controller.update_user)
