supermercado = {
    "cafe": 15.00,
    "achocolatado": 10.00,
    "pao": 4.00,
    "arroz": 10.00
}

print(f"Itens para comprar (chave): {supermercado.keys()}")
print(f"Itens para comprar (valor): {supermercado.values()}")
print(f"Itens para comprar (item): {supermercado.items()}")

print("**"*30)

for chave,valor in supermercado.items():
    print(f"O {chave} custa R$ {valor}")
    
#ESCOLHENDO PRODUTO
print("**"*30)
while True:
    produto = input("Informe o produto a ser pesquisado (escreva 'fim' para sair): ")
    if produto == 'fim':
        break
    if produto in supermercado:
        print(f"O produto {produto} custa R$ {supermercado[produto]}")
    else:
        print(f"O produto {produto} não foi encontrado")

