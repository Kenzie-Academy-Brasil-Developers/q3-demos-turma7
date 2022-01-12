class Teacher:
    quarters = ("Q1", "Q2", "Q3", "Q4")

    def __init__(self, name: str, quarter: str) -> None:
        self.name = name
        self.quarter = self.set_quarter(quarter)
        self.meeting_id = None

    def set_quarter(self, quarter):
        return quarter.upper() if quarter.upper() in self.quarters else "Q1"

    def schedule_1_on_1(self, time: int, someone: str) -> None:
        print(f"Successfully scheduled meeting with {someone} by {self.__repr__()}")

    def create_meeting(self, meeting_id: str) -> None:
        self.meeting_id = meeting_id
        print(f"Meeting <{self.meeting}> criada")

    def __repr__(self) -> str:
        return f"<{self.name}:{self.quarter}>"
