from flask import Blueprint
from app.controllers import user_controller

bp = Blueprint("user", __name__, url_prefix="/users")

bp.get("/<int:user_id>")(user_controller.get_user_by_id)
bp.get("/<int:user_id>/orders")(user_controller.get_user_orders)
bp.get("/<int:user_id>/invoices")(user_controller.get_user_invoices)
