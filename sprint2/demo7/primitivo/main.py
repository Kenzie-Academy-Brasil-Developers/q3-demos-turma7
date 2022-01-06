import re
import requests
from requests.exceptions import JSONDecodeError
from exceptional_exceptions import UnderDog

zip_code = input("Digite o CEP: ")

mo = re.match(r"\d{5,8}", zip_code)

try:
    if not mo:
        raise UnderDog(zip_code)
    r = requests.get(f"https://viacep.com.br/ws/{zip_code}/json/")
    print(r.json())
except JSONDecodeError as e:
    print(f"Error: {e}")
