from flask import Flask, Blueprint


def init_app(app: Flask) -> None:
    bp = Blueprint("bp", __name__, url_prefix="/api")

    from .user_route import bp_user

    bp.register_blueprint(bp_user)

    app.register_blueprint(bp)
