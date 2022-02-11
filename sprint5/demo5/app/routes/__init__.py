from flask import Blueprint, Flask
from app.routes.call_record_route import bp as bp_call_record


bp_api = Blueprint("api", __name__, url_prefix="/api")


def init_app(app: Flask):
    bp_api.register_blueprint(bp_call_record)

    app.register_blueprint(bp_api)
