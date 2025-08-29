compra = [10.2, 3.35, 16.3, ["tomate", "sabonete", "arroz"]]#lista compra, com o 4º item sendo outra lista (sublista)
print(compra)

produtos = compra[3]#lista produtos, recebendo APENAS o 4º item (sublista) da lista compra
print(produtos)

total = compra[0]+compra[1]+compra[2]#calculando o total dos 3 primeiros itens da lista compra
print(total)

letra = ["a", "b", "c"]
num = [2,4,6]
tudo = [letra,num]#lista 'tudo' que terá 2 sublistas nas posições 0 e 1, respectivamente
print(tudo)
print(f"Letras: {tudo[0]}")
print(f"Números: {tudo[1]}")