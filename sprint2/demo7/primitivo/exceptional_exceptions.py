class UnderDog(Exception):
    def __init__(self, zip):
        self.message = f"The zip you've entered({zip}) is invalid."

    def __str__(self):
        return self.message
