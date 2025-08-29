numeros = []

while True:
    numero = int(input("Digite números (0 para sair): "))
    if numero == 0:
        break
    numeros.append(numero)

repetidos = []
nao_repetidos = []    
for i in numeros:
    if numeros.count(i) > 1:
        repetidos.append(i)
    else:
        nao_repetidos.append(i)
        
numeros.sort()
repetidos.sort()
nao_repetidos.sort()

print(f"Lista original: {numeros}")
print(f"Lista dos repetidos: {repetidos}")
print(f"Lista dos não repetidos: {nao_repetidos}")