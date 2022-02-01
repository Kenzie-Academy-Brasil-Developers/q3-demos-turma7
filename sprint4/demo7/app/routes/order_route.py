from flask import Flask, Blueprint
from app.controllers import order_controller

bp = Blueprint("order", __name__, url_prefix="/orders")

bp.get("")(order_controller.get_orders)
