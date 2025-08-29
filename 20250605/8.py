maior = 0
menor = 999999
qnt = 0
soma = 0
media = 0

for i in range(7):
    numero = int(input("Digite um número: "))
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero
    soma = soma + numero
    qnt = qnt + 1

media = soma / qnt
print(f"O maior número digitado é {maior}")
print(f"O menor número digitado é {menor}")
print(f"A média dos números lidos é {media}")