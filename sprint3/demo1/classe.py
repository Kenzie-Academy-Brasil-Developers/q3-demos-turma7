from datetime import datetime as dt

# Transforma os type hintings em string
# from __future__ import annotations


class Person:
    # Atributos de classe
    life_expectancy = 90  # Imutável
    shopping_list = ["Violao"]  # Mutável

    # Métodos de instancia
    def __init__(self, name: str, cpf: str, pet: bool = False):
        # Atributos de instancia
        self.name = name
        self.cpf = cpf
        self.pet = pet
        self.created_at = dt.now().strftime("%d/%m/%Y %H:%M:%S")
        self.partner = None
        self.steps = 0

    # Método de instancia (self)
    def walk(self, quantidade: int = 1):
        self.steps += quantidade

    # Método de instancia e dunder method (self e __ __)
    def __repr__(self) -> str:
        return f"<{self.name}:{self.cpf}>"

    # Método estático (nao recebe self como primeiro parametro)
    @staticmethod
    def marry(person1: "Person", person2: "Person"):
        # person1.partner = person2
        # person2.partner = person1
        person1.partner, person2.partner = person2, person1


# 1 - Atributos de classe
# p1 = Person()
# p2 = Person()
# p3 = Person()
# p1.life_expectancy = 100
# print(p1.life_expectancy)
# print(p2.life_expectancy)
# print(p3.life_expectancy)

# 2 - prints de atributo de classe mutável (lista)
# p1.shopping_list.append("Teclado")
# print(p1.shopping_list)
# print(p2.shopping_list)
# print(p3.shopping_list)

# 3 - instanciando classe com inicializador
# p1 = Person("person1", "1111")
# print(p1)
# p2 = Person("person2", "2222")
# p3 = Person("person3", "3333")
# print(p1.name)
# print(p2.name)
# print(p3.name)
# print(p1.__dict__)

p1 = Person("person1", "1111")
p2 = Person("person2", "2222", True)
p3 = Person("person3", "3333")

# print(p1.__dict__)

# 4 - método estático
# Person.marry(p1, p2)
# print(p1.__dict__)
# print(p2.__dict__)

# p3.marry(p1, p2)
# print(p1.__dict__)
# print(p2.__dict__)
# Não consigo chamar um método de instancia diretamente pela classe
# Person.walk(10)
