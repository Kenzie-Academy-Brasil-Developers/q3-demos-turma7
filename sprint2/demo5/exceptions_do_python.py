# https://docs.python.org/pt-br/3.9/library/exceptions.html

commands = [
    "print"# "int{}", "abs{}", "aslkdj", 234
]

for comando in commands:
    # try:
    #     eval(comando.format("()"))
    # except NameError as e:
    #     print("Esse dado não é um comando Python")
    eval(f"{comando}('Texto a imprimir')")

try:
    "CÓDIGO QUE DEVERIA ESTAR EXECUTANDO"
except KeyboardInterrupt:
    "RETORNE A PARTE QUE ESTÁ FERRANDO O SISTEMA"