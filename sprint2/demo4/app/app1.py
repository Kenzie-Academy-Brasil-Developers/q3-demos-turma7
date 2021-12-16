from flask import Flask, request, jsonify

app = Flask(__name__)


# # 127.0.0.1:5000/
# # Query params -> ? where &
# @app.get("/params")
# def query():
#     query_params = request.args
#     return jsonify(query_params)


@app.get("/rota_din/<variavel>")
@app.get("/rota_din/")
def query1(variavel=None):
    if variavel == None:
        return "PÁGINA DA ROTA DINÂMICA"
    
    d = {
        "kenzie": {"Página": "Valores"},
        "academy": {"Página2": "Valores2"}

    }

    return d.get(variavel.lower(), "<h1>404, Página não encontrada</h1>"), 200 if variavel in d else 404 