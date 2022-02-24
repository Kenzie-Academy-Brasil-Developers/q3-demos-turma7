from flask import current_app, render_template
from flask_mail import Message, Mail
from pdfkit import from_string
from os import getenv
from app.models.user_model import UserModel


def pdfkit(email: str):
    mail: Mail = current_app.mail
    user: UserModel = UserModel.query.filter_by(email=email).first()

    pdf = from_string(render_template("pdf/template.html", nome=user.name, produtos=user.products), False)

    msg = Message(
        subject="PDFKit",
        sender=getenv("MAIL_USERNAME"),
        recipients=["q3.daily@gmail.com"],
        html=render_template("email/template.html", edu=":edu:"),
    )

    msg.attach("pdfkit.pdf", "application/pdf", pdf)

    mail.send(msg)

    return {"stts": "ok"}, 200
