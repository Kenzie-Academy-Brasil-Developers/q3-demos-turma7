from flask import Blueprint, Flask
from app.routes.user_route import bp as bp_user
from app.routes.order_route import bp as bp_order


bp_api = Blueprint("api", __name__, url_prefix="/api")


def init_app(app: Flask):
    bp_api.register_blueprint(bp_user)
    bp_api.register_blueprint(bp_order)

    app.register_blueprint(bp_api)
