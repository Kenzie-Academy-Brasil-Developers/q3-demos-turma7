class Manager:
    def schedule_1_on_1(self, time: int, someone: int):
        if time < 30:
            print(f"Successfully schedule meeting with {someone}")
        else:
            print("Time is too long... Please select a time under 30min")

    def orgazine_kanban(self):
        print("Organizing kanban... ")
