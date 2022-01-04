import io

f = io.StringIO("O rato roeu a roupa do rei de Roma")

[print(line) for line in f.readlines()]
