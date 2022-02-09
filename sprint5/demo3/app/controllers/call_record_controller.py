from flask import request, jsonify
from http import HTTPStatus
from flask import current_app

from app.configs.database import db
from app.models.call_record_model import CallRecord
import ipdb


def create_record():
    data = request.get_json()

    record = CallRecord(**data)
    # print(record)

    db.session.add(record)
    db.session.commit()
    # print(record.__dict__)
    # ipdb.set_trace()

    # return record.serializer(), HTTPStatus.CREATED
    return jsonify(record), HTTPStatus.CREATED


def get_records():
    return {"msg": "GET RECORDS"}
