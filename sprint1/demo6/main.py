import os; os.system("clear"); print("\n\n")
################### CÓDIGO ACIMA SÓ ESTÁ SENDO USADO PARA LIMPAR O TERMINAL #################################


# LIST COMPREHENSION: TERNARY OPERATOR, NESTED IF's, OTHER COMPREHENSIONS (OPERADOR)
# "ESQUERDA" if False else "DIREITA"
# print([var if True else "depois else" for var in "kenzie"])
# [num for num in range(10) if num % 2 == 0 if num > 4]
# (x for x in range(10)) # GENERATOR
# [x, y for x in range(10) for y in "abcd"]

# LISTS AND THEIR FUNCTIONS
# append   count    insert   remove
# clear    extend   reverse
#   index  pop      sort


# OTHER COMPREHENSIONS
# {x, y for x in range(10) for y in "abcd"}


# EXEC vs EVAL: PARSERS


# PACKING vs UNPACKING, MAPPING: ARGS vs KWARGS

# def f(param1, param2):
#     print(param1, param2)

# def f(*V):
#     return list(V)

# print(f(1, 2, 4, 4, 5, {1: 5}))


def g(**kwargs):
    for chave, valor in kwargs.items():
        print(chave, valor, sep=": ")

g(ch1=9, ch2=10)


# ARGUMENTO POSICIONAL


# REFERENCE vs VALUE
# copy, SHALLOW COPY

import copy
l1 = []
l2 = l1
l3 = copy.deepcopy(l2) # CÓPIA PERFEITA 
l4 = l1.copy() # CÓPIA SUPERFICIAL, N1




# VALOR é independente de reatribuição
num1 = 10
num2 = num1


# EVAL DE f recebendo 5


################### CÓDIGO ABAIXO SÓ ESTÁ SENDO USADO PARA LIMPAR O TERMINAL #################################
print("\n\n")
