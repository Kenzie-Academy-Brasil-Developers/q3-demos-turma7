import time


def leitor_binario_de_arquivos(file):
    data = "Arquivo não encontrado"
    start_time = time.time()
    try:
        # Roda primeiro
        # Abrir os olhos
        f = open(file, mode="rb")
        data = f.read()

    except FileNotFoundError as e: # Luz forte ou olhos costurados
        # Roda se uma exceção ocorre
        
        raise
        
    else:
        # É executado se o try funcionou
        # Enxergar
        f.close()
        return data
    finally:
        # Sempre executa
        # Batida do coração
        end_time = time.time()
        time_elapsed = end_time - start_time
        print(time_elapsed)


read = leitor_binario_de_arquivos("kenzie.wav")
print(read)
