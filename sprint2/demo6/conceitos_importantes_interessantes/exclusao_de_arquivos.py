import os

# Excluir arquivos simples
try:
    os.remove("./diretorio/arquivo.txt")
    print("Arquivo removido com sucesso!")
except FileNotFoundError:
    print("Arquivo não encontrado!")

# Excluir diretórios
# try:
#     os.rmdir("diretorio")
#     print("Diretorio removido com sucesso!")
# except FileNotFoundError:
#     print("Arquivo não encontrado!")

# Não muito recomendado
# os.system("rm arquivo.txt")
# os.system("cls")


# A FUNÇÃO NATIVA TENDE A ISOLAR E SER AGNÓSTICA, OU SEJA O SISTEMA OPERACIONAL NÃO INTERFERE