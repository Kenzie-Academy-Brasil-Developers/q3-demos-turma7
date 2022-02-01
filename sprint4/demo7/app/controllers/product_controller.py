from flask import jsonify
from http import HTTPStatus


def get_products():
    return jsonify({"msg": "Obter todos os produtos"}), HTTPStatus.OK
