import os
os.system("clear") # WORKAROUND

for f in range(2):
    print("")

### CÓDIGO ACIMA NÃO ESTÁ SENDO USADO DIRETAMENTE 

## Automatizando tarefas massantes - Al Sweigart
# git -> https://github.com/asweigart/
# site -> https://automatetheboringstuff.com/

## CONTROLE DE FLUXO

# import json # dumps, loads


# Booleans: truthys, falsys
# Os valores vazios representam False # E os valores preenchidos, representam True
# bool(0)
# bool([])
# bool(())
# bool({"": 1})
# 4 == 4
# 4 != 4

# True & False são da familia dos inteiros
# [True, 5, 7, False, ""]

# if, else, else if & elif: aninhamento -> mutipla verificação, DICIONÁRIO

# nome = input("DIGITE SEU NOME: ")

# Verificação simples
# if nome == "toranja":
#     print("O nome é igual")

# # Verificação standard
# if not nome:  # bool(nome) redundante
#     print("Você não preencheu")

# BLOCO DE IF COMEÇA SEMPRE COM IF
# if True:
#    print("PASSOU NO IF")
#    f = 5

# # elif 4 > 2:
# #     print("OUTRO BLOCO DE IF")

# else:
#     if 4 > 2:
#         print("OUTRO BLOCO")
#     else:
#         print("")
#         print("FAZ PARTE DO BLOCO")

# if True:
#     if False:
#         if False:
#             pass

# dias_da_semana = {
#     1: print,
#     2: "segunda",
#     7: "sábado"

# }

# user_digitou = 1

# dias_da_semana.get(user_digitou, "ESSE CARA REPRESENTA O ELSE")("FUNCIONOU COMO SE FOSSE O PRINT")


# bloco de instrução: indentação e escopo global vs escopo de função
# TEASER PRÓXIMA DEMO, 

# for - while: iteráveis
for variavel in "kenzie academy brasil":
    pass  # Pass, ..., 5
    print(variavel)


# MAIS DE UMA VERIFICAÇÃO

if (4 > 5) and (4 * 2 - 3 < 0):
    print()

# continue, break, pass

# operador ternário: one-liners

# 

# print(f) VARIÁVEIS DE ESCOPO GLOBAL
# print(variavel)

### CÓDIGO ABAIXO NÃO ESTÁ SENDO USADO DIRETAMENTE 



for i in range(2):
    print("")
