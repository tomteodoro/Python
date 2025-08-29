medias_alunos = []

def classificar_medias(medias):
    situacao = {
        "Aprovado": 0,
        "Recuperação": 0,
        "Reprovado": 0
    }
    for media in medias:
        if media >= 7:
            situacao["Aprovado"] += 1
        elif media < 7 and media >=5:
            situacao["Recuperação"] += 1
        else:
            situacao["Reprovado"] += 1
    return situacao

while True:
    media = float(input("Digite a média do aluno (-1 para sair): "))
    if media == -1:
        break
    medias_alunos.append(media)
    
print(f"A quantidade de alunos com as situações Aprovado, Recuperação e Reprovado é {classificar_medias(medias_alunos)}")