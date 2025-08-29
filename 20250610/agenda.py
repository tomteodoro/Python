agenda = []

#MENU
while True:
    print("--- AGENDA DE TAREFAS ---")
    print("1- Inserir tarefa")
    print("2- Excluir tarefa")
    print("3- Alterar tarefa")
    print("4- Mostrar agenda")
    print("5- Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":

        data = input("Digite a data da tarefa (Ex: 09/11/1945): ")
        tarefa = input("Digite a tarefa: ")
        situacao = input("Digite a situação (FAZER, FAZENDO ou FEITO): ").upper()
       
        if situacao in ["FAZER", "FAZENDO", "FEITO"]:
            nova_tarefa = {"data": data, "tarefa": tarefa, "situacao": situacao}
            agenda.append(nova_tarefa)
            print("Tarefa adicionada")
        else:
            print("Situacao invalida")

    elif opcao == "2":
        print("\nTarefas:")
        for i in range(len(agenda)):
            print(f"{i + 1}. {agenda[i]['data']} - {agenda[i]['tarefa']} [{agenda[i]['situacao']}]")
       
        indice = int(input("Digite o número da tarefa que deseja excluir: ")) - 1

        if 0 <= indice < len(agenda):
            agenda.pop(indice)
            print("Tarefa excluída com sucesso!")
        else:
            print("Número inválido")
   
    elif opcao == "3":

        print("\nTarefas cadastradas: ")
        for i in range (len(agenda)):
            print(f"{i + 1}. {agenda[i]['data']} - {agenda[i]['tarefa']} [{agenda[i]['situacao']}]")
       
        indice = int(input("Digite o número da tarefa que deseja alterar: ")) - 1

        if 0 <= indice < len(agenda):
            print("Deixe em branco se não quiser mudar nada.")
            nova_data = input("Nova data: ")
            nova_tarefa = input("Nova tarefa: ")
            nova_situacao = input("Nova situação (FAZER, FAZENDO, FEITO)").upper()

            if nova_data:
                agenda[indice]["data"] = nova_data
            if nova_tarefa:
                agenda[indice]["tarefa"] = nova_tarefa
            if nova_situacao:
                agenda[indice]["situacao"] = nova_situacao
            elif nova_situacao:
                print("Situação inválida! mantem a anterior...")
           
            print("Tarefa atualizada!")

        else:
            print("Numero invalido")

    elif opcao == "4":

        if not agenda:
            print("Nenhuma tarefa cadastrada")
        else:
            print("--- AGENDA COMPLETA ---")
            for i in range(len(agenda)):
                t = agenda[i]
                print(f"{i + 1}. {t['data']} - {t['tarefa']} [{t['situacao']}]")
    elif opcao == "5":
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Tente novamente")