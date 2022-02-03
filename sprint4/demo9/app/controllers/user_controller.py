from flask import jsonify, request
from http import HTTPStatus
from app.models.user_model import User
from psycopg2.errors import UniqueViolation


def get_users():
    # from app.models import conn

    email = request.args.get("email")

    if email:
        users = User.read_users_by_email(email)
        serialized_users = User.serialize_user(users)

        return jsonify(serialized_users), HTTPStatus.OK

    users = User.read_users()

    users_list = User.serialize_user(users)

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

    # Sobrescrevendo para transformar em dict (chave, valor)
    serialized_user = User.serialize_user(inserted_user)

    return jsonify(serialized_user), HTTPStatus.CREATED


def update_user(user_id):
    payload = request.get_json()

    updated_user = User.update_user(user_id, payload)

    if not updated_user:
        return {"error": f"user id {user_id} not found"}, HTTPStatus.NOT_FOUND

    serialized_user = User.serialize_user(updated_user)

    return jsonify(serialized_user), HTTPStatus.OK
