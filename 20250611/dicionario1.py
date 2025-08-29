contatos = {}

while True:
    nome = input("Digite o nome (ou 'fim' para encerrar): ").lower()
    if nome == "fim":
        break

    telefone = input(f"Digite o telefone: ")
    email = input(f"Digite o e-mai: ")

    contatos[nome] = [telefone, email]

for nome,(telefone,email) in contatos.items():
    print(f"Nome: {nome} | Telefone: {telefone} | E-mail: {email}")
