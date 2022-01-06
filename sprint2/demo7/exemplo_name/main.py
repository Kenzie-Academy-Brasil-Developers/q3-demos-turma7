from modulo import *

# if __name__ == "__main__":
#     print("O módulo externo não foi executado")
#     f()

class MinhaClass:
    pass

    def __str__(self) -> str:
        return "Esse é o objeto MinhaClass"

    def __eq__(self, __o: object) -> bool:
        object != __o

instancia = MinhaClass()
print(instancia)