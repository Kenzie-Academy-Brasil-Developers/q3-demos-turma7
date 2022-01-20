from flask import jsonify, request
from http import HTTPStatus
from app.models.dev_model import Dev


def get_devs():
    devs_list = Dev.get_all()

    devs_list = list(devs_list)

    Dev.serialize_dev(devs_list)

    # chave _id contém como valor um objeto ObjectId
    # print(devs_list[0])
    # for dev in devs_list:
    #     dev.update({"_id": str(dev["_id"])})

    # Dicionario pós tratamento
    # print(devs_list[0])

    return jsonify(devs_list), HTTPStatus.OK


def create_dev():
    data = request.get_json()
    dev = Dev(**data)

    dev.post_dev()
    Dev.serialize_dev(dev)
    # list(dev) -> [dev]
    # dev._id = str(dev._id)

    # print("DEV DICT  ->>>", dev.__dict__)

    return jsonify(dev.__dict__), HTTPStatus.CREATED


def delete_dev(dev_id):
    deleted_dev = Dev.delete_dev(dev_id)
    Dev.serialize_dev(deleted_dev)

    return jsonify(deleted_dev), HTTPStatus.OK


# /devs?nome=rick&email=rick@mail.com
# data = request.args -> dicionario
# data['nome'] = data['nome'].title()
# data -> {"nome": "Rick", "email": "rick@mail.com"}
