from app.classes.teacher import Teacher
from app.classes.enabler import Enabler
from app.classes.manager import Manager
from app.classes.instructor import Instructor

# t1 = Teacher("Teache1", "2222222222")
# print(t1)
# print(t1.__dict__)
# t1.create_meeting("30218391278382")
# print(t1.__dict__)
# t1.schedule_1_on_1(60, "MaisOutroAlguem1")

# e1 = Enabler("Enable1", "Q3", ["Coach1", "Coach2"])
# # print(e1)
# # print(e1.__dict__)
# # print(e1.quarters)
# e1.schedule_1_on_1(60, "Coach1")

# t1 = Teacher("Teache1", "2222222222")
# print(t1)
# print(t1.__dict__)
# t1.create_meeting("30218391278382")
# print(t1.__dict__)

# m1 = Manager()
# m1.schedule_1_on_1(29, "OutroAlguem")
# m1.orgazine_kanban()

i1 = Instructor("Instructor1", "Q4")
# print(i1)
# print(i1.__dict__)
# i1.schedule_1_on_1(60, "MaisAlguem1")
i1.batatinha = "batata"
print(i1.__dict__)
