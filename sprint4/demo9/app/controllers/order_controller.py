from flask import jsonify, request
from http import HTTPStatus

from app.models.order_model import Order


def get_orders():
    # Lista de tuplas
    orders = Order.select_all()

    # order é uma tupla
    orders_serialized = [Order.serializer(order) for order in orders]

    return jsonify(orders_serialized), 200


def get_order_by_id(order_id: int):
    # Passando lista de chaves, tanto de orders quanto de users, serao
    # retornados colunas dinamicas
    # desired_keys = ["order_id", "email", "order_date", "account_balance"]
    # order = Order.select_order_by_id(order_id, desired_keys)

    # Nao passando lista de chaves, todas as chaves de orders serao usadas
    order = Order.select_order_by_id(order_id)

    return jsonify(order), HTTPStatus.OK
