from sqlalchemy.orm.session import Session
from flask import request, jsonify

# from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound
from flask import current_app
from http import HTTPStatus
from werkzeug.exceptions import NotFound

from app.models.call_record_model import CallRecord
from app.configs.database import db
import ipdb


def get_record_by_id(call_record_id: int):
    session: Session = db.session
    base_query = session.query(CallRecord)

    # record = session.query(CallRecord).filter(CallRecord.id == call_record_id).first()
    # record = session.query(CallRecord).get(call_record_id)
    # record = base_query.filter_by(id=call_record_id).first()
    # record = base_query.filter_by(source=111111113).all()

    # if not record:
    #     return {"error": f"id {call_record_id} not found"}, HTTPStatus.NOT_FOUND

    # try:
    #     # record = base_query.filter_by(id=call_record_id).one()
    #     record = base_query.filter_by(source=111111113).one()
    # except NoResultFound:
    #     return {"error": f"id {call_record_id} not found"}, HTTPStatus.NOT_FOUND
    # except MultipleResultsFound:
    #     return {"error": f"multiple results found"}, HTTPStatus.OK
    try:
        record = base_query.filter_by(id=call_record_id).first_or_404(
            description="id not found"
        )
    except NotFound as e:
        return {"error": e.description}, HTTPStatus.NOT_FOUND

    return jsonify(record), HTTPStatus.OK


def get_records():
    session: Session = db.session
    base_query = session.query(CallRecord)

    page = request.args.get("page", 1, type=int)
    per_page = request.args.get("per_page", 3, type=int)
    records = base_query.order_by(CallRecord.id).paginate(page, per_page)

    return jsonify(records.items), HTTPStatus.OK


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
