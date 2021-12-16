from flask import Flask, request, jsonify
from .estados import estados, estados_completos
from json import dumps, loads
import pickle

app = Flask(__name__)

# FAKE, MOCK -> MOCKING BIRD

@app.get("/todos_os_estados")
def liste_estados():
    return jsonify(estados)


@app.get("/estados/<estado>")
def filtro(estado: str):
    filtrado = [item for item in estados_completos if item["sigla"] == estado]

    return jsonify(filtrado)


@app.get("/estados/<string:estado>/<string:cidade>")
def filtro2(estado, cidade):
    filtrado = [item for item in estados_completos if estado in item["nome"] == estado]
    retorno = filtrado[0]["sigla"]

    return jsonify(retorno)






# PUT -> Atualizar : "nome": "kenzie" -> "nome": "academy"
# POST -> "nome": "kenzie" -> "nome": "academy"
# PATCH: Atulização parcial




