from flask import Flask, jsonify, request
from http import HTTPStatus
from app.exc.invalid_plate import InvalidPlateError
from app.exc.spot_already_taken import SpotAlreadyTakenError

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

    # print(c.__dict__)

    try:
        c = Car(**request.get_json())
        return c.save(), HTTPStatus.CREATED
    except InvalidPlateError as e:
        return {"msg": e.message}, e.status_code
    except AlreadyInParkingSlotError as e:
        return {"msg": f"{e.message}"}, e.status_code
    except SpotAlreadyTakenError as e:
        return {"msg": e.message}, e.status_code
