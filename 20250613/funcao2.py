import math

def menu():
    print("\nBEM-VINDO AO MENU:")
    print("1 - Calcular equação de Bhaskara")
    print("2 - Calcular área do quadrado")
    print("3 - Calcular volume do cubo")
    print("4 - Sair do programa")
    opcao = int(input("Escolha uma opção: "))
    return opcao

def bhaskara(a, b, c):       
    delta = b**2 - 4*a*c
    if delta < 0:
        return print("A equação não possui raízes reais.")
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        return x1, x2
        
def area_quadrado(lado):
    area = lado ** 2
    return area

def volume_cubo(aresta):
    volume = aresta ** 3
    return volume

while True:
    escolha = menu()
    if escolha == 1:
        a = int(input("Digite o valor de a: "))
        if a == 0:
            print("O valor de 'a' não pode ser zero em uma equação do segundo grau.")
        else:
            b = int(input("Digite o valor de b: "))
            c = int(input("Digite o valor de c: "))
            print(f"Para os valores informados: a={a}, b={b} e c={c}, x' e x'' são: {bhaskara(a, b, c)}")

    elif escolha == 2:
        lado = float(input("Digite o valor do lado do quadrado: "))
        print(f"A área do quadrado é: {area_quadrado(lado):.2f}")

    elif escolha == 3:
        aresta = float(input("Digite o valor da aresta do cubo: "))
        print(f"O volume do cubo é: {volume_cubo(aresta):.2f}")

    elif escolha == 4:
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida.")