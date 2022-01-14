class InvalidPlateError(Exception):
    default_message = "Plates must be in AAA-1111 format"
    status_code = 400

    def __init__(self, message=default_message, status_code=status_code):
        self.message = message
        self.status_code = status_code
