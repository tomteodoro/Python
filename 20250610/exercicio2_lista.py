palavras = []

while True:
    palavra = input("Digite palavras (0 para sair): ")
    if palavra == "0":
        break
    palavras.append(palavra)

qual_palavra = input("Qual palavra deseja contar quantas vezes apareceu? ")
conta_palavra = palavras.count(qual_palavra)
        
print(f"A palavra '{qual_palavra}' foi digitada {conta_palavra} vez(es)!")