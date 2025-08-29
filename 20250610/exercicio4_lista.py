import random

nomes = []
sorteados = []

while True:
    nome = input("Digite nomes (0 para sair): ")
    if nome == "0":
        break
    nomes.append(nome)
    
while nomes:
    escolhido = random.choice(nomes)
    sorteados.append(escolhido)
    nomes.remove(escolhido)
    
print("\nOrdem de sorteio:")
for i in range(len(sorteados)):
    print(f"{sorteados[i]}")