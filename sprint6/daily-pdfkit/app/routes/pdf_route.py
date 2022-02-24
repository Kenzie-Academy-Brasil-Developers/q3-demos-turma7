from flask import Blueprint
from app.controllers.pdfkit_controller import pdfkit


bp_pdf = Blueprint("bp_pdf", __name__, url_prefix="/pdfkit")

bp_pdf.get("/<string:email>")(pdfkit)
