# CRIANDO ARQUIVO
nome_do_arquivo = "20250729\\exemplo4.txt"

# ESCREVENDO NO ARQUIVO
with open(nome_do_arquivo, "w") as arquivo:
    arquivo.write("Primeira\n")
    arquivo.write("Segunda\n")
    arquivo.write("Terceira\n")

# ABRINDO ARQUIVO
with open(nome_do_arquivo, "r") as arquivo:
    # LINHA TODA
    linha = arquivo.readline()
    print(f"1: {linha}")
    # SOMENTE 5 CARACTERES
    linha = arquivo.readline(5)
    print(f"2: {linha}")
    # SOMENTE 10 CARACTERES OU FIM DA LINHA
    linha = arquivo.readline(10)
    print(f"3: {linha}")
    # SOMENTE 10 CARACTERES OU FIM DA LINHA
    linha = arquivo.readline(10)
    print(f"4: {linha}")