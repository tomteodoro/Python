# Solicita ao usuário o número da tabuada que deseja treinar
numero = int(input("Digite o número que deseja treinar na tabuada: "))

acertos = 0
erros = 0

# Loop para os multiplicadores de 1 a 10
for i in range(1, 11):
    resposta_usuario = int(input(f"{numero} x {i} = "))
    resultado_correto = numero * i

    if resposta_usuario == resultado_correto:
        print("CORRETO!")
        acertos += 1
    else:
        print(f"QUE PENA, VOCÊ ERROU. O VALOR CORRETO É {resultado_correto}.")
        erros += 1

# Exibe o total de acertos e erros
print("\n=== RESULTADO FINAL ===")
print(f"Total de acertos: {acertos}")
print(f"Total de erros: {erros}")
