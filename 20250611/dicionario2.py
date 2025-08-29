alunos = {}

while True:
    nome = input("Digite o nome do aluno (ou 'fim' para encerrar): ").strip()
    if nome.lower() == "fim":
        break

    media = float(input(f"Digite a média de {nome}: "))

    if media >= 7:
        situacao = "Aprovado"
    elif media >= 5:
        situacao = "Recuperação"
    else:
        situacao = "Reprovado"

    alunos[nome] = {
        "nota": media,
        "situação": situacao
    }

for nome in alunos:
    print(f"Aluno(a): {nome} | Média: {alunos[nome]['nota']} | Situação: {alunos[nome]['situação']}")
