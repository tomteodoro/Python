frutas = {}

for i in range(3):
    nome = input(f"Digite o nome da fruta: ")
    preco = float(input(f"Digite o preço por quilo da fruta: "))
    frutas[nome] = preco
    
for chave, valor in frutas.items():
    print(f"A fruta {chave} custa R$ {valor:.2f} por kg")
