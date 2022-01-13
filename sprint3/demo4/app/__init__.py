from flask import Flask, jsonify, request
from http import HTTPStatus

# from app.services.json_handler import read_json, write_json
from app.models.car_model import Car
from app.exc.already_in_parking_slot import AlreadyInParkingSlotError

app = Flask(__name__)

# FILENAME = 'parking_lot.py'


@app.get("/cars")
def retrive():
    # Parte 1 - JSON puro
    # return jsonify(read_json(FILENAME)), HTTPStatus.OK

    # Parte 2 - Classes com JSON
    return jsonify(Car.get_cars()), HTTPStatus.OK


@app.post("/cars")
def create():
    # Parte 1 - JSON puro
    # return write_json(FILENAME, data), HTTPStatus.CREATED

    # Parte 2 - Classes com JSON
    c = Car(**request.get_json())
    # print(c.__dict__)

    try:
        return c.save(), HTTPStatus.CREATED
    except AlreadyInParkingSlotError:
        return {"msg": "Plate already parked!"}, HTTPStatus.CONFLICT
