# VENV

""" Variáveis de ambiente são nomeadas dinamicamente """

# DECORATOR: Vínculo, Regras e alteração do comportamento, aninhamento
# maiusculo = str.upper
# def metamorfose(fnc):
#     return fnc


# def  borboleta():
#     print("Borboleta voando. E passando de folha em folha.")


# @metamorfose  NÃO CRIA VÍNCULO AINDA!!!
# def lagarta():
#     print("Lagarta comendo folhas.")



# # lagarta = metamorfose(borboleta)
# lagarta()

# imprima = metamorfose(print)
# imprima("ALGO")




# def gritar(texto: str):
#     return f"{texto.upper()}!!!"


# def sussurrar(texto: str):
#     texto = f"{texto.lower()}..."
#     return texto


# def falar(texto: str, funcao):
#     text = funcao(texto)
#     return texto


# texto_externo = "Kenzie"
# print(sussurrar(texto_externo))
# print(gritar(texto_externo))


def verficador_de_texto(texto):
    def gritar(texto):
        return f"{texto.upper()}!!!"

    def sussurrar(texto: str):
        return f"{texto.lower()}..."

    if len(texto) < 4:
        return gritar
    else:
        return sussurrar




# print(verficador_de_texto("k")("kenzie")) 

def decorator(func):
    def wrapper(texto):
        print("COISAS ACONTECENDO ANTES")
        func(texto)
        print("COISAS ACONTECENDO DEPOIS")
    
    return wrapper


@decorator  ## JÁ CRIA VÍNCULO
def imprime(texto):
    print(texto)


imprime("Kenzie")


# from functools import cache


# def for_rapido():
#     a = 0
#     for numero in range(100000000):
#         a += 1
#     return a

# print(for_rapido())

