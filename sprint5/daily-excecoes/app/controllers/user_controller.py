from . import UserModel
from app.services.user_service import validate_body
from typing import Tuple
from http import HTTPStatus
from flask import current_app, jsonify, request
from werkzeug.exceptions import BadRequest
from sqlalchemy.exc import IntegrityError
from psycopg2.errors import UniqueViolation



def insert_user() -> Tuple:
    try:
        validated = validate_body(request.get_json(), name=str, email=str)
        user = UserModel(**validated)

        current_app.db.session.add(user)
        current_app.db.session.commit()

        return jsonify(user), HTTPStatus.CREATED

    except BadRequest as e:
        return e.description, e.code

    except IntegrityError as e:
        if isinstance(e.orig, UniqueViolation):
            return {"error": "email already exists"}, HTTPStatus.CONFLICT


def retrieve_users() -> Tuple:
    users = UserModel.query.all()

    return jsonify(users)
