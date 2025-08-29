nome_arquivo = "alunos_notas.txt"

with open(nome_arquivo, "a") as arquivo:
    while True:
        nome = input("Digite o nome do(a) aluno(a) (ou 'sair' para encerrar): ")
        if nome.lower() == "sair":
            print("Saindo...")
            break
        nota = input(f"Digite a nota do(a) {nome}: ")
        arquivo.write(f"{nome} = {nota}\n")

print(f"\nDados salvos no arquivo: {nome_arquivo}")
