alunos = []
prova1 = []
prova2 = []
situação = []
medias = []
for n in range(10):
    nomes = input("Digite seu nome: ").lower()
    nota_1 = float(input("qual é sua primeira nota: "))
    nota_2 = float(input("qual é sua segunda nota: "))
    media = (nota_1 + nota_2)/2 
    medias.append(media)   
    alunos.append(nomes)
    prova1.append(nota_1)
    prova2.append(nota_2)
    if media >= 7:
        situação.append("aprovado")
    else:
        situação.append("reprovado")
        
media_p1 = sum(prova1)/10
media_p2 = sum(prova2)/10
print(f"Essa é a lista de pessoas {alunos}. Junto a isso, essa é sua primeira nota {prova1} essa é a segunda nota {prova2}.") 
print(f"Essa é a lista de pessoas aprovadas ou reprovadas {situação}.")
print(F"Essa é a media dos alunos [{media}] e a média da primeira e da segunda prova ({media_p1}) e ({media_p2})" )