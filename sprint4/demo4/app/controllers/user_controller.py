from flask import jsonify, request
from http import HTTPStatus
from app.models.user_model import User
from psycopg2.errors import UniqueViolation


def get_users():
    # from app.models import conn
    users = User.read_users()

    user_keys = ["id", "email", "birthdate", "children", "married", "account_balance"]
    users_list = [dict(zip(user_keys, user)) for user in users]

    return jsonify(users_list), HTTPStatus.OK
    # return jsonify({"msg": "Obter todos os usuarios"}), HTTPStatus.OK


def create_user():
    data = request.get_json()

    user = User(**data)

    # Tupla com os valores do registro
    try:
        inserted_user = user.create_user()

    except UniqueViolation as e:
        return (
            jsonify({"error": "email already exists"}),
            HTTPStatus.UNPROCESSABLE_ENTITY,
        )

    user_keys = ["id", "email", "birthdate", "children", "married", "account_balance"]
    # Sobrescrevendo para transformar em dict (chave, valor)
    inserted_user = dict(zip(user_keys, inserted_user))

    return jsonify(inserted_user), HTTPStatus.CREATED
