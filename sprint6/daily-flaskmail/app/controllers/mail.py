from flask import current_app, render_template
from flask_mail import Message, Mail
from os import getenv


def flask_mail() -> tuple:
    mail: Mail = current_app.mail

    msg = Message(
        subject="Flask Mail",
        sender=getenv("MAIL_USERNAME"),
        recipients=["q3.daily@gmail.com"],
        html=render_template("email/template.html", nome=":Edu:")
    )

    mail.send(msg)

    return {"stts": "ok"}, 200
