from app.services.json_handler import read_json, write_json
from app.services.car_service import (
    check_if_plate_is_already_parked,
    check_if_spot_is_already_taken,
    validate_plate,
    get_spot_by_plate,
)
from app.exc.already_in_parking_slot import AlreadyInParkingSlotError
from app.exc.spot_already_taken import SpotAlreadyTakenError


class Car:
    FILENAME = "parking_lot.json"

    def __init__(
        self, plate: str, company: str, model: str, color: str, spot: str
    ) -> None:
        self.plate = validate_plate(plate)
        self.company = company
        self.model = model
        self.color = color
        self.spot = spot.upper()

    @classmethod
    def get_cars(cls) -> list[dict]:
        return read_json(cls.FILENAME)

    def save(self):
        #
        car = self.__dict__
        if check_if_plate_is_already_parked(self.FILENAME, car["plate"]):
            plate_spot = get_spot_by_plate(self.FILENAME, car["plate"])
            raise AlreadyInParkingSlotError(plate=car["plate"], spot=plate_spot)
        elif check_if_spot_is_already_taken(self.FILENAME, car["spot"]):
            raise SpotAlreadyTakenError(spot=car["spot"])

        return write_json(self.FILENAME, car)
