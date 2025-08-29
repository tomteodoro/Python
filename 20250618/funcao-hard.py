import string

def validar_senha(senha):
    maiuscula = False
    minuscula = False
    numero = False
    especial = False
    if len(senha) >= 8:
        for caractere in senha:
            if caractere.isupper():
                maiuscula = True
            if caractere.islower():
                minuscula = True
            if caractere.isdigit():
                numero = True
            if caractere in string.punctuation:
                especial = True
        if maiuscula and minuscula and numero and especial:
            return True

while True:
    senha = input("Digite uma senha forte (Mínimo 8 caracteres, pelo menos 1 letra maiúscula, 1 minúscula, 1 número e 1 caractere especial): ")
    if validar_senha(senha):
        print("Senha válida!")
        break
    else:
        print("Senha inválida! Tente novamente...")