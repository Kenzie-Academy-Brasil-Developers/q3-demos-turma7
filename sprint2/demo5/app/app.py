import werkzeug.exceptions
from flask import Flask, request, jsonify, render_template


app = Flask(__name__)


var = None

@app.get("/")
def home():
    try:
        return "7"
    except:
        return "O Flask não sabe lhe dar com inteiros"


@app.get("/get")
def get_algo():
    try:
        return "1"
    except KeyboardInterrupt:
        return "5"
    finally:
        print("Código executado com sucesso")


@app.post("/")
def set_algo():
    return "Página de configuração"


@app.get("/configs/<key>")
def set_configs(key):
    entity = {"idade": "3", "nome": "Kenzie"}
    try:
        configs = entity[key]
        return a
    except (NameError, KeyError):
        return "Chave incorreta"

# ESSE HANDLER NÃO TEM NADA A VER COM PYTHON

@app.errorhandler(404)
def not_found(e):
    return render_template("404.html")
