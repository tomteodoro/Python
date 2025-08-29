numero = int(input("Digite um número que deseja treinar a tabuada: "))
acertos = 0
erros = 0

for i in range(1,10):
    resposta = int(input(f"{numero} x {i} = "))
    resultado = numero * i

    if resposta == resultado:
        print("CORRETO")
        acertos = acertos + 1
    else:
        print(f"QUE PENA, VOCÊ ERROU. A RESPOSTA CORRETA É {resultado}")
        erros = erros + 1

print(f"Total de Acertos: {acertos}")
print(f"Total de Erros: {erros}")