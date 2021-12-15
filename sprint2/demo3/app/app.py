# VARIÁVEIS DE AMBIENTE


from flask import Flask, redirect, url_for
from os import environ
import os
from time import sleep, time


app = Flask(__name__)


@app.route("/")
def kenzie():
    return f"<h1> BEM VINDO A HOME {environ.get('user')}!! </h1>"



@app.route("/acesso-negado")
def acessonegado():
    return "ACESSO NEGADO BIXÃO"



@app.route("/comum")  # ENDPOINTS
def commonuser():
    return "TODOS OS USERS CONSEGUEM ACESSAR AQUI, {}".format(os.getenv("user"))


@app.route("/acesso")
def func_acesso():
    if environ.get("user") == "usermaster":
        return "VOCÊ TEM ACESSO A ESSA ÁREA!"
    else:
        sleep(2)
        return redirect(url_for("acessonegado"))


@app.route("/<nome>")
def variavel(nome: str):
    return f"BEM VINDO {nome}"

# ERROS: [Errno 98] Address already in use
# BRUTE: kill -9 $(lsof -ti tcp:443)
