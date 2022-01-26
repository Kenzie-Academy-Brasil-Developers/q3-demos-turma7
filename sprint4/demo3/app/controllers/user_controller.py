from flask import jsonify
from http import HTTPStatus
from app.models.user_model import User


def get_users():
    users = User.read_users()

    user_keys = ["id", "email", "birthdate", "children", "married", "account_balance"]

    users_list = [dict(zip(user_keys, user)) for user in users]

    return jsonify(users_list), HTTPStatus.OK
    # return jsonify({"msg": "Obter todos os usuarios"}), HTTPStatus.OK
