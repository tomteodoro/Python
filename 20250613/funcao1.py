#FUNCAO SOMA
def soma(n1,n2):
    soma = n1+n2
    return soma

#FUNCAO SUBTRACAO
def subtracao(n1,n2):
    sub = n1-n2
    return sub

#CODIGO PRINCIPAL
print('Bem vindo a calculadora')
num1=int(input('Digite o primeiro numero: '))
num2=int(input('Digite o segundo numero: '))
op = int(input('Digite 1 para somar e 2 para subtrair'))
if op == 1:
    print(f'O valor de soma {num1} + {num2} = {soma(num1,num2)}')
elif op ==2:
    print(f'O valor da subtração {num1} - {num2} = {subtracao(num1,num2)}')
else:
    print('Comando invalido!!')