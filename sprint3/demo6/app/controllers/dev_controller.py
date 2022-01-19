from app.models.dev_model import Dev
from flask import jsonify
from http import HTTPStatus


def retrieve():
    devs_list = Dev.get_all()

    devs_list = list(devs_list)

    # chave _id contém como valor um objeto ObjectId
    # print(devs_list[0])
    for dev in devs_list:
        dev.update({"_id": str(dev["_id"])})

    # Dicionario pós tratamento
    # print(devs_list[0])

    return jsonify(devs_list), HTTPStatus.OK
