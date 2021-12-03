import os
os.system("clear")
################################################


# Livro: Python Fluente - Luciano Ramalho

# EXTENSÃO PARA VISUALIZAÇÃO DE CÓDIGO: PARA FINS DIDÁTICOS: python preview, ou site: pythontutor.com

## FUNÇÕES e BUILTINS, COMPREHENSIONS: list
# print(repr("""
# """))

# GERALMENTE UTILIZADOS PARA CONDIÇÕES
# all()
# any()

# repr() - str()

# ZIP, ENUMERATE
# inc = 0
# for letra in "kenzie":
#     print(letra, inc)
#     inc += 1

f = ["toranja", "bergamota", "figo"]
q = ["cítrica", "cítrico", "não cítrico"]

# for indice, letra in enumerate("kenzie"):
#     print(indice, letra)
    

for fruta, qualidade in zip(f, q):
    print(fruta, qualidade)

# KEYWORDS: continue, break, pass
# import keyword
# keyword.kwlist

# for numero in "12345":
#     if numero == "3":
#         print("OPA, NOME LIMPO")
#         continue
#         # pass, não modifica fluxo
#     print("PAGUE O QUE ME DEVE")  # cobrança de dívida

# FUNÇÕES EMBUTIDAS
# breakpoint()

# CRIANDO e TRABALHANDO COM FUNÇÕES

# GLOBAL
# salario = 5
# def f():
#     # LOCAL, INNER VARS
#     global salario  # Não é muito legal, não muito recomendado
#     print(salario)

# f()


# GLOBAL vs NONLOCAL vs LOCAL

# def escopo_local():
#     fruta = "figo"

#     def funca_mais_interna():
#         nonlocal fruta
#         local_local = 6
        
    # nonlocal local_local  NÃO É POSSÍVEL ENCHERGAR
    # print(local_local)



# FUNCTION - PROCEDURE - MODULE
# def retorno():
#     return 6

# def procedure():
#     print()
#     abs(-1)

# # MODULO
# str.capitalize()

# 
# def recebe_mas_nao_retorna(numero, num1, num2):  # VARIÁVEIS: parâmetro, assinatura
#     pass

# print(recebe_mas_nao_retorna(1, 2, 3))

# def recebe_e_retorna_outro_valor(num3=None):
#     return 0

# print(recebe_e_retorna_outro_valor(120938))


# def retorna_algo_associado_ao_argumento(arg_passado):
#     return arg_passado * 5


# print(retorna_algo_associado_ao_argumento("3"))


# transforma_em_maiusculo = str.upper

# print(transforma_em_maiusculo("askjdhaksjdhaksjdh"))

# RETURN

# O FOR NÃO CRIA UM AMBIENTE LOCAL
for qualquer in "kenzie":
    pass

print(qualquer)


mult = lambda asdjkl: asdjkl * asdjkl
print(mult(9))

# STREAM -> 

################################################
print("")