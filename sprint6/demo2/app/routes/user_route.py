from flask import Blueprint
from app.controllers import user_controller

bp = Blueprint("users", __name__, url_prefix="/users")

bp.post("/login")(user_controller.login_user)
bp.post("")(user_controller.create_user)
bp.get("")(user_controller.list_users)
bp.get("/<user_id>")(user_controller.get_user_by_id)
