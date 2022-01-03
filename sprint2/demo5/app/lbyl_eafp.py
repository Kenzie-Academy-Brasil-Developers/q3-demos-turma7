# ERROR -> EXCEPTION

# LOOK BEFORE YOU LEAP: LBYL

# person = {"nome": "Victor", "idade": 27, "profissão": "matemático"}
person = {"nome": "Victor", "idade": 27}

# if "nome" in person and "idade" in person and "profissão" in person:
#     print("Meu nome é {nome}. Eu tenho {idade} anos de idade e sou {profissão}".format(**person))
# else:
#     print("Faltam algumas chaves.")

# EASIER TO ASK FOR FORGIVENESS THAN PERMISSION: EAFP
# try:
#     print("Meu nome é {nome}. Eu tenho {idade} anos de idade e sou {profissão}".format(**person))
# except:
#     print("Faltam algumas chaves.")


# finally:
#     print("ESSE TRECHO SEMPRE É EXECUTADO")

try:
    print("Meu nome é {nome}. Eu tenho {idade} anos de idade e sou {profissão}".format(**person))
except NameError:
    print("Essa var não existe")
except KeyError:
    print("Chave incorreta/não existe")

# ERROS SÃO COISAS QUE A MÁQUINA NÃO ENTENDE, NÃO FAZ SENTIDO PARA MÁQUINA

# try:
#     print(
# except:
#     print("PARTE II")


# EXCEPTIONS SÃO ERROS LÓGICOS OU DE REGRA DE NEGÓCIO
numero = 0
try:
    print(5/numero)
except:
    print("PARTE II")


# class KenzieError(Exception):
#     code = 404
#     description = "Você tentou acessar o kenzie mode"
    
#     def return_message(description):
#         return description

#     def __str__(self) -> str:
#         return super().__str__()

# try:
#     4 + ""
# except KenzieError():
#     print("Kenzie error")


try:
    5 + ""
except TypeError as error:
    print(error)

# RAISE