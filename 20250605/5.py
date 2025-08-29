idade_mulher = 0
qnt_mulher = 0
media_mulher = 0
idade_homem = 0
qnt_homem = 0
media_homem = 0
media_grupo = 0

for i in range(5):
    idade = int(input("Digite a sua idade: "))
    sexo = input("Digite o seu sexo (M/H): ").upper()
    if sexo == "M":
        qnt_mulher = qnt_mulher + 1
        idade_mulher = idade_mulher + idade
    else:
        qnt_homem = qnt_homem + 1
        idade_homem = idade_homem + idade

if qnt_mulher > 0:
    media_mulher = idade_mulher / qnt_mulher
    print(f"A idade média das mulheres é: {media_mulher:.2f}")
if qnt_homem > 0:    
    media_homem = idade_homem / qnt_homem
    print(f"A idade média dos homens é: {media_homem:.2f}")
if qnt_mulher > 0 or qnt_homem > 0:
    media_grupo = (idade_mulher + idade_homem) / (qnt_mulher + qnt_homem)
    print(f"A idade média do grupo é: {media_grupo:.2f}")