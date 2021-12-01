import os
os.system("clear") # WORKAROUND

for i in range(2):
    print("")

import sys
import time
from time import sleep


# print("KENZIE")

# LIVRO(S) DE INDICAÇÃO: Python by example - Nichola Lacey, How to Make Mistakes in Python - Mike Pirnat

## Tipos em Python: List, Set, Tuples, Dict: indice vs chave

# Inicialização:

lista = list([3, 6, 10, "", 1.2])  # Homogênia, a = []
conjuntos = set({1, 5, 9, "", 3.141592}), # f = set(), ELIMINAR DUPLICATAS
tupla = ()
dicionario = dict({"chave": 923875, "dog": "cachorro"})

# ACESSANDO VALORES DE UM DICT INSEGURAMENTE
# print(dicionario)
# print(dicionario["6"])

# "" SEGURAMENTE
print(dicionario.get("cat", "ESSA CHAVE NÃO EXISTE"))

# Fixo vs Não fixo: hashable

# Único vs Replicável: set, list

# Mutável e imutável: list, dict, set <-> string, tuple, int, float
f = [1, 2, 3]
f.reverse()
print(f)
f.clear()
print(f)

# Funções embutidas de cada tipo: acesse pelo objeto
list.clear()
set.add()
str.capitalize()

# FUNÇÃO COM ANOTAÇÃO PONTO

# Valor vs Referência: SERÁ ABORDADO PRÓXIMA DEMO

## APLICAÇÃO

# Avião: Número dos assentos, posição física dos assentos: coordenada -> (Dimensões janelas jogos)





### CÓDIGO ABAIXO É 
for i in range(2):
    print("")