numeros = []
soma_numeros = 0
multiplica_numeros = 1
maior = 0
menor = 999999

while True:
    numero = int(input("Digite números (0 para sair): "))
    if numero == 0:
        break
    numeros.append(numero)
    soma_numeros = soma_numeros + numero
    multiplica_numeros = multiplica_numeros * numero
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero
        
print(f"Os números informados foram: {numeros}")
print(f"A soma de todos os números informados é: {soma_numeros}")
print(f"A multiplicação de todos os números informados é: {multiplica_numeros:,}")
print(f"O maior número informado é: {maior}")
print(f"O menor número informado é: {menor}")