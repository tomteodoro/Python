# Lista para armazenar os números digitados
numeros = []

print("Digite números (0 para encerrar):")
while True:
    n = int(input("Número: "))
    if n == 0:
        break
    numeros.append(n)

# Lista sem repetição
sem_repeticao = sorted(list(set(numeros)))

# Lista de números repetidos
repetidos = []
for num in set(numeros):
    if numeros.count(num) > 1:
        repetidos.append(num)
repetidos.sort()

# Ordenando a lista original
numeros.sort()

# Exibindo as listas
print("\nLista original:", numeros)
print("Sem repetição:", sem_repeticao)
print("Números repetidos:", repetidos)
