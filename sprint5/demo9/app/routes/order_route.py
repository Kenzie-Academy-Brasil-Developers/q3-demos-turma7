from flask import Blueprint
from app.controllers import order_controller

bp = Blueprint("order", __name__, url_prefix="/orders")

bp.get("/<int:order_id>")(order_controller.get_order_by_id)
bp.get("/<int:order_id>/products")(order_controller.get_order_products)
bp.get("/<int:order_id>/products/query")(order_controller.get_order_products_query)

bp.post("/<int:order_id>/products")(order_controller.add_item)
