nome_produtos = []
quant_produtos = []
preco_produtos = []
#************************
media_abaixo = []
media_acima = []
preco_organizado = []
#************************
nome_produto_barato = ''
nome_produto_caro = ''
#************************
total = 0
total_compra = 0
quant_produtos_total = 0
soma_cada_preco = 0
#*************************
print("======== LISTA DE COMPRAS ========")
for i in range (3):
    print("---------------------")
    nome = input("Digite o nome do produto: ")
    nome_produtos.append(nome)
    quant = int(input("Digite a quantidade do produto: "))
    quant_produtos.append(quant)
    quant_produtos_total += quant
    preco_uni = float(input("Digite o preço unitário do produto: "))
    preco_produtos.append(preco_uni)
    total += preco_uni*quant
    soma_cada_preco += preco_uni
#************************************
media_precos = soma_cada_preco/3
for i in range (3):
    if preco_produtos[i] >= media_precos:
        media_acima.append(nome_produtos[i])
    else:
        media_abaixo.append(nome_produtos[i])
#**************************************
total_compra += total
preco_organizado += preco_produtos
preco_organizado.sort()
nome_produto_barato = nome_produtos[preco_produtos.index(preco_organizado[0])]
nome_produto_caro = nome_produtos[preco_produtos.index(preco_organizado[-1])]
#*************************************
print(f"\n| Produto mais caro: {nome_produto_caro} |\n| Produto mais barato: {nome_produto_barato} |\n| Total da compra: R${total} |")
print(f"Média do preço de todos os produtos: R${media_precos:.2f}")
print(f"\n| Produtos abaixo da média: {media_abaixo} |\n| Produtos acima ou igual a média: {media_acima} |")