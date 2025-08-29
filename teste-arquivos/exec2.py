with open("nomes.txt", "r") as arquivo:
    linhas = arquivo.readlines()

x = 1
for linha in linhas:
    print(f"{x}: {linha}")
    x = x + 1
