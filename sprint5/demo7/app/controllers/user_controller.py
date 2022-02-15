from http import HTTPStatus
from flask import jsonify

from app.models.user_model import User
from app.configs.database import db


def get_user_by_id(user_id: int):
    user: User = User.query.get(user_id)

    if not user:
        return {"error": f"user id {user_id} not found"}, HTTPStatus.NOT_FOUND

    return jsonify(user), HTTPStatus.OK


def get_user_orders(user_id: int):
    user: User = User.query.get(user_id)

    if not user:
        return {"error": f"user id {user_id} not found"}, HTTPStatus.NOT_FOUND

    return jsonify(user.orders), HTTPStatus.OK


def get_user_invoices(user_id: int):
    user: User = User.query.get(user_id)

    if not user:
        return {"error": f"user id {user_id} not found"}, HTTPStatus.NOT_FOUND

    # user.orders -> lista de objetos Order
    return (
        jsonify([order.invoice for order in user.orders if order.invoice is not None]),
        HTTPStatus.OK,
    )
