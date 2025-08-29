with open("nomes.txt", "w") as arquivo:
    for i in range(3):
        nome = input("Digite o nome: ")
        arquivo.write(f"{nome}\n")
