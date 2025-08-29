nome = input("Nome: ")
media = float(input(f"Média de {nome}: "))
situacao = ""
aluno = {}
if media >= 7:
    situacao = "Aprovado"
else:
    situacao = "Reprovado"

aluno["nome"] = nome
aluno["media"] = media
aluno["situacao"] = situacao

print(f"Nome é igual a {aluno['nome']}")
print(f"Média é igual a {aluno['media']}")
print(f"Situação é igual a {aluno['situacao']}")