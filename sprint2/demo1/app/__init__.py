from flask import Flask

app = Flask(__name__)


@app.route("/home", methods=["POST"])
def qualquer_outro_nome():
    return "DEMO DE FLASK", 201
