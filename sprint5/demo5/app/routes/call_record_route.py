from flask import Blueprint
from app.controllers import call_record_controller

bp = Blueprint("call_record", __name__, url_prefix="/call-records")

bp.get("")(call_record_controller.get_records)
bp.get("/<int:call_record_id>")(call_record_controller.get_record_by_id)
bp.post("")(call_record_controller.create_record)
bp.patch("/<int:record_id>")(call_record_controller.update_record)
bp.delete("/<int:record_id>")(call_record_controller.delete_record)
