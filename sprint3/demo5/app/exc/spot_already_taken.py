class SpotAlreadyTakenError(Exception):
    default_message = "Spot already taken!"
    spot = "not informed"
    status_code = 409

    def __init__(self, message=default_message, status_code=status_code, spot=spot):
        self.message = message + " " + spot
        self.status_code = status_code
