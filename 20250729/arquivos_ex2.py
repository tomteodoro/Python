nome_do_arquivo = "20250729\\exemplo.txt"

with open(nome_do_arquivo, "w") as arquivo:
    arquivo.write("Hello, SESI!\n")
    arquivo.write("Segunda linha de texto.\n")

#ADICIONANDO A UM ARQUIVO
with open(nome_do_arquivo, "a") as arquivo:
    arquivo.write("Linha adicionada ao final do arquivo.\n")