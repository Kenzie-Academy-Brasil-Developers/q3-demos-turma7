from app.classes.teacher import Teacher
from app.classes.manager import Manager


class Instructor(Teacher, Manager):
    def __init__(self, name: str, quarter: str) -> None:
        super().__init__(name, quarter)
        # Manager.__init__()
        # Teacher.__init__()
