import datetime

arquivo_nome = "presencas.txt"

def registrar_presenca():
    nome = input("Digite o nome do aluno: ")
    dataHora = datetime.datetime.now()
    dataHora = dataHora.strftime("%d/%m/%Y %H:%M:%S")
    with open(arquivo_nome, "a") as arq:
        arq.write(f"{nome} - {dataHora}\n")
    print("Presença registrada com sucesso!\n")

def listar_presencas():
    print("\n=== Lista de Presenças ===")
    with open(arquivo_nome, "r") as arq:
        linhas = arq.readlines()
        cont = 1
        for linha in linhas:
            print(f"{cont}. {linha}")
            cont = cont + 1

def menu():
    while True:
        print("\n=== Sistema de Presença ===")
        print("[1] Registrar presença")
        print("[2] Ver lista de presença")
        print("[0] Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            registrar_presenca()
        elif opcao == "2":
            listar_presencas()
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.\n")

menu()