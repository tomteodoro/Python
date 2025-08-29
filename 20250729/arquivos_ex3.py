nome_do_arquivo = "20250729\\exemplo.txt"

#ABRINDO O ARQUIVO COMO SOMENTE LEITURA
with open(nome_do_arquivo, "r") as arquivo:
    # Lendo o conteúdo do arquivo
    conteudo = arquivo.read()

#IMPRIMINDO O ARQUIVO
print(conteudo)