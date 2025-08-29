alunos = {}
soma = 0

for i in range(3):
    nome = input(f"Digite o nome do aluno: ")
    nota = float(input(f"Digite a nota da aluno: "))
    alunos[nome] = nota
    soma += nota
    
for aluno, nota in alunos.items():
    print(f"{aluno}: {nota}")

media = soma / 3
print(f"Média da turma: {media:.2f}")
