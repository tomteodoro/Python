numeros = []
par = []
impar = []

def verifica_par_impar(num):
    if num % 2 == 0:
        numVerificado = "par"
    else:
        numVerificado = "ímpar"
    return numVerificado

while True:
    numero = int(input("Digite um número (-1 para sair): "))
    if numero == -1:
        break
    numeros.append(numero)
    if verifica_par_impar(numero) == "par":
        par.append(numero)
    else:
        impar.append(numero)        

numeros.sort(reverse=True)
par.sort()
impar.sort()
print(f"A lista de todos os números, em ordem decrescente, é: {numeros}")
print(f"A lista de todos os números PARES, em ordem crescente, é: {par}")
print(f"A lista de todos os números ÍMPARES, em ordem crescente, é: {impar}")