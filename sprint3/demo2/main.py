# from app.classes_import.classe1 import Hello
# from app.classes_import.classe2 import Goodbye

from app.classes_import import Hello, Goodbye


print("main.py", __name__)

# h = Hello("Brasil")
# h.hello()

h = Hello("Brasil")
h.hello()

g = Goodbye()
g.goodbye(h)
