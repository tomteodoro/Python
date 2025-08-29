contagem_temp_alta=0
contagem_temp_febre=0
contagem_temp_febril=0
contagem_temp_normal=0

temperatura_normal=0
temperatura_alta=0
temperatura_febril=0
temperatura_febre=0

while True:
    sair=str(input(" Vc quer calcular se esta com febre?(enter para continuar e 'n' para interromper): "))
    sair_mi=sair.lower()
    if sair_mi=="n":
       break
    temperatura=float(input("Digite a sua temperatura corporal:  "))
    nome=str(input("Digite seu nome: "))
    if temperatura > 39:
      contagem_temp_alta = contagem_temp_alta+1
      temperatura_alta=temperatura_alta+temperatura
      print("Você,",nome,"está com febre alta, procure um médico logo")
    elif temperatura <= 39 and temperatura >=38.1:
      contagem_temp_febre = contagem_temp_febre+1
      temperatura_febre=temperatura_febre+temperatura
      print("Você,",nome,"está com febre, fique atento e tome algum remédio")
    elif temperatura <= 38 and temperatura >=37.3:
       contagem_temp_febril = contagem_temp_febril+1
       temperatura_febril=temperatura_febril+temperatura
       print("Você,",nome,"está em estado febril, por enquanto não deve se preocupar")
    elif temperatura <= 37.2:
       temperatura_normal=temperatura_normal+temperatura
       contagem_temp_normal = contagem_temp_normal+1
       print("Você,",nome,"não tem febre, sua temperatura está normal")
contagem_temp_total=contagem_temp_alta+contagem_temp_febre+contagem_temp_febril+contagem_temp_normal
temperaturas=temperatura_alta+temperatura_febre+temperatura_febril+temperatura_normal

if contagem_temp_alta >0:
   media_alta=temperatura_alta/contagem_temp_alta
   print(f"Quantidade de pessoas com febre alta: {contagem_temp_alta}")
   print(f"Média alta: {media_alta:.2f}")
if contagem_temp_febre>0:
    media_febre=temperatura_febre/contagem_temp_febre
    print(f"Quantidade de pessoas com febre: {contagem_temp_febre}")
    print(f"Média febre: {media_febre:.2f}")
if contagem_temp_febril>0:
    media_febril=temperatura_febril/contagem_temp_febril
    print(f"Quantidade de pessoas em estado febril: {contagem_temp_febril}")
    print(f"Média febril: {media_febril:.2f}")
if contagem_temp_normal>0:
   media_normal=temperatura_normal/contagem_temp_normal
   print(f"Quantidade de pessoas com temperatura normal: {contagem_temp_normal}")
   print(f"Média normal: {media_normal:.2f}")
if contagem_temp_total >0:
    media_geral=temperaturas/contagem_temp_total
    print(f"Quantidade de temperaturas informadas: {contagem_temp_total}")
    print(f"Média geral: {media_geral:.2f}")