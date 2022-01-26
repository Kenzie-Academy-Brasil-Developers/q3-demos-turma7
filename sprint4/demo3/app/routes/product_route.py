from flask import Flask, Blueprint
from app.controllers import product_controller

bp = Blueprint("products", __name__, url_prefix="/api")


# def product_route(app: Flask):
#     @bp.get("/products")
#     def retrieve():
#         return product_controller.get_products()


# @bp.get("/products")
# def retrieve():
#     return product_controller.get_products()


bp.get("/products")(product_controller.get_products)
