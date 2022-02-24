from flask import Blueprint
from app.controllers.mail_controller import flask_mail


bp_mail = Blueprint("bp_mail", __name__, url_prefix="/flask_mail")

bp_mail.get("")(flask_mail)
