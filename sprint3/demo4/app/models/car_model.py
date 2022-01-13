from app.services.json_handler import read_json, write_json
from app.services.car_service import check_if_plate_is_already_parked
from app.exc.already_in_parking_slot import AlreadyInParkingSlotError


class Car:
    FILENAME = "parking_lot.json"

    def __init__(
        self, plate: str, company: str, model: str, color: str, spot: str
    ) -> None:
        self.plate = plate
        self.company = company
        self.model = model
        self.color = color
        self.spot = spot

    @classmethod
    def get_cars(cls) -> list[dict]:
        return read_json(cls.FILENAME)

    def save(self):
        #
        car = self.__dict__
        if check_if_plate_is_already_parked(self.FILENAME, car["plate"]):
            raise AlreadyInParkingSlotError

        return write_json(self.FILENAME, car)
