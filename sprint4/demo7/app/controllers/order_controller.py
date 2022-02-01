from flask import jsonify, request
from http import HTTPStatus

from app.models.order_model import Order


def get_orders():
    # Lista de tuplas
    orders = Order.select_all()

    # order é uma tupla
    orders_serialized = [Order.serializer(order) for order in orders]

    return jsonify(orders_serialized), 200
