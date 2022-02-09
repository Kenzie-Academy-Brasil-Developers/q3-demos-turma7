from flask import Blueprint
from app.controllers import call_record_controller

bp = Blueprint("call_record", __name__, url_prefix="/call-records")

bp.get("")(call_record_controller.get_records)
bp.post("")(call_record_controller.create_record)


# app.get('/')
# def get_():
# ...