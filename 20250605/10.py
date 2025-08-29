numero = int(input("Digite um número para treinar a tabuada: "))
total_acertos = 0
total_erros = 0

for i in range(1,11):
    resultado = int(input(f"{numero} x {i} = "))
    gabarito = numero * i
    if resultado == gabarito:
        print("CORRETO")
        total_acertos += 1
    else:
        print(f"QUE PENA, VOCÊ ERROU, O VALOR CORRETO É {gabarito}")
        total_erros += 1

print(f"Total de acertos: {total_acertos}")
print(f"Total de erros: {total_erros}")