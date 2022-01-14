from app.exc.invalid_plate import InvalidPlateError
from app.services.json_handler import read_json


def check_if_plate_is_already_parked(filepath: str, plate: str) -> bool:
    cars_list = read_json(filepath)

    # return [car for car in read_json(filepath) if car["plate"] == plate]

    for car in cars_list:
        if car["plate"] == plate:
            return True

    return False


def get_spot_by_plate(filepath: str, plate: str) -> str:
    for car in read_json(filepath):
        if car["plate"] == plate:
            return car["spot"]


def check_if_spot_is_already_taken(filepath: str, spot: str) -> bool:
    for car in read_json(filepath):
        if car["spot"] == spot:
            return True

    return False


def validate_plate(plate: str):
    # AAA-1234
    if (
        plate[:3].isalpha()
        and plate[4:].isnumeric()
        and len(plate) == 8
        and plate[3] == "-"
    ):
        return plate.upper()

    raise InvalidPlateError
