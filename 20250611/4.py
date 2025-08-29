palavra = input("Digite uma palavra: ").lower()
quantidade = {}

for letra in palavra:
    if letra in quantidade:
        quantidade[letra] += 1
    else:
        quantidade[letra] = 1

print(quantidade)
