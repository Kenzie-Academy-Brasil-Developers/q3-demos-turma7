class AlreadyInParkingSlotError(Exception):
    default_message = "car already in parking spot"
    spot = "not informed"
    plate = "plate not informed"
    status_code = 409

    def __init__(
        self, message=default_message, status_code=status_code, spot=spot, plate=plate
    ):
        # 'not informed plate car already in parking spot not informed'
        self.message = plate + " " + message + " " + spot
        self.status_code = status_code
