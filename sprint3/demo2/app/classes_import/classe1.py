# from typing import Union
import typing

# JAMAIS
# from typing import *

print("classe1.py", __name__)


class Hello:
    phone: str = "2103921039120"

    def __init__(self, country: str) -> None:
        self.country = country

    def hello(self) -> typing.Union[None, str]:
        x = 0
        if x > 1:
            print("Hello")
        else:
            return "String else"


# Exemplo de import dentro de escopo
def func():
    from typing import Union
