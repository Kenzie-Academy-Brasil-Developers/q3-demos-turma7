# Funciona só se o arquivo executado for o classe2.py diretamente
# from classe1 import Hello

# Melhor importar direto do módulo invés de por um intermediario
# import typing
# from .classe1 import typing

# Necessario ao testar executando classes2.py
# from .classe1 import Hello


print("classe2.py", __name__)


class Goodbye:
    def goodbye(self, another_class):
        print(f"Goodbye {another_class.country}")


# h = Hello("Brasil")
# h.hello()

# g = Goodbye()
# g.goodbye(h)
