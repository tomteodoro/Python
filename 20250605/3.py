while True:
    usuario = input("Digite o seu nome de usuário: ")
    senha = input("Digite a sua senha: ")
    if usuario == senha:
        print(f"O nome de usuário e a senha não podem ser iguais! Tente novamente.")
    else:
        print(f"Cadastro realizado com sucesso!")
        break