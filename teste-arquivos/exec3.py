with open("nomes.txt", "r") as original:
    conteudo = original.read()

with open("copia.txt", "w") as copia:
    copia.write(conteudo)