from app.controllers.user_controller import insert_user, retrieve_users
from flask import Blueprint


bp_user = Blueprint("bp_user", __name__, url_prefix="/users")

bp_user.get("")(retrieve_users)
bp_user.post("")(insert_user)
