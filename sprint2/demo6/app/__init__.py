import os
from flask import Flask, request
import pickle
from models.model1 import *


app = Flask(__name__)

def escrever(conteudo):
    try:
        with open("./files/example.txt", "a") as f:
            f.write(conteudo)
            f.write("\n")
    except FileNotFoundError:
        os.mkdir("./files")
        escrever(conteudo)

@app.post("/lista")
def cadastrar():
    """ Essa função cadastra itens no "banco de dados" """

    data = request.get_json()
    quantidade = data.get("quantidade")
    item = data.get("item")
    conteudo = f"Devo comprar {quantidade} de {item}"
    escrever(conteudo)

    return {"message": "Item adicionado a lista!"}, 201


@app.post("/upload")
def save_body():
    print(request.data)

    return "NÃO É QUE SUBIU", 200
