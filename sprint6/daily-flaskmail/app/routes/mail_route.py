from flask import Blueprint
from app.controllers.mail import flask_mail


bp_mail = Blueprint("bp_mail", __name__)

bp_mail.get("/")(flask_mail)
