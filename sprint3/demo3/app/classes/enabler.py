# Classe1 extends Classe2
from app.classes.teacher import Teacher


class Enabler(Teacher):
    def __init__(self, name: str, quarter: str, coaches: list[str]) -> None:
        super().__init__(quarter=quarter, name=name)
        self.coaches = coaches

    def schedule_1_on_1(self, time: int, someone: str) -> None:
        if someone in self.coaches:
            return super().schedule_1_on_1(time, someone)

        print(f"{someone} is not in my coach list... 1_0_1 not scheduled")
