from flask import Flask, Blueprint


def init_app(app: Flask) -> None:
    bp = Blueprint("bp_api", __name__, url_prefix="/api")
    from .mail_route import bp_mail
    from .pdf_route import bp_pdf

    bp.register_blueprint(bp_mail)
    bp.register_blueprint(bp_pdf)

    app.register_blueprint(bp)
