# If you fail to plan, you are palling to fail - Benjamin Franklin

import os
from datetime import datetime
from werkzeug.utils import safe_join
from werkzeug.utils import secure_filename
from flask import Flask, request, jsonify # safe_join
from werkzeug.http import HTTP_STATUS_CODES

UPLOAD_DIRECTORY = "./uploads"

os.makedirs(UPLOAD_DIRECTORY, exist_ok=True)

app = Flask(__name__)


@app.get("/")
def home():
    return "home", 200


@app.post("/body")
def body_save_file():
    extension = request.headers.get("Content-Type", "").split("/")[-1]
    filename = f"{str(datetime.now())}.{extension}".replace(" ", "_")
    file_path = safe_join(UPLOAD_DIRECTORY, filename)

    print(file_path)

    with open(file_path, "wb") as file:
        file.write(request.data)

    return {"msg": f"{file_path} CREATED!!"}, 201


# Exemplo simples de uso de enumerators
@app.post("/form")
def form_save_file():
    files = list(request.files)

    if not len(files):
        return {"msg": "Envie pelo menos 1 arquivo."}, 406

    uploaded_list = []

    for file in files:
        received_file = request.files[file]
        filename = secure_filename(received_file.filename)
        file_path = safe_join(UPLOAD_DIRECTORY, filename)
        received_file.save(file_path)
        uploaded_list.append(filename)

    return jsonify(uploaded_list), 201