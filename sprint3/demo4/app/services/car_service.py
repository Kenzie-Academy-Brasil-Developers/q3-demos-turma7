from app.services.json_handler import read_json


def check_if_plate_is_already_parked(filepath: str, plate: str) -> bool:
    cars_list = read_json(filepath)

    for car in cars_list:
        if car["plate"] == plate:
            return True

    return False
