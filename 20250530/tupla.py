nomes = []
p1s = []
p2s = []
medias = []
situacoes = []

for i in range(10):
    nome = input("Nome: ")
    p1 = float(input("Nota P1: "))
    p2 = float(input("Nota P2: "))
    
    media = (p1 + p2) / 2
    if media >= 7.0:
        situacao = "Aprovado" 
    else:
        situacao = "Reprovado"
    
    nomes.append(nome)
    p1s.append(p1)
    p2s.append(p2)
    medias.append(media)
    situacoes.append(situacao)

media_p1 = sum(p1s) / 10
media_p2 = sum(p2s) / 10



print("\nMédia da turma na P1: {:.2f}".format(media_p1))
print("Média da turma na P2: {:.2f}".format(media_p2))
