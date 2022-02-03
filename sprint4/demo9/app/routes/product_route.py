from flask import Blueprint
from app.controllers import product_controller

bp = Blueprint("products", __name__, url_prefix="/products")


bp.get("")(product_controller.get_products)
bp.post("")(product_controller.create_product)
