pessoas = {}

while True:
    nome = input("Digite o nome (ou 'fim' para encerrar): ")
    if nome.lower() == "fim":
        break
    idade = int(input(f"Digite a idade: "))
    pessoas[nome] = idade

for nome, idade in pessoas.items():
    if idade > 18:
        print(f"{nome} = {idade}")
