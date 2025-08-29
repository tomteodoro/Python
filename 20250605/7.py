#print(f"Os números entre 5 e 100 que são divisíveis por 7, mas não são múltiplos de 5 são: ")
for i in range(5,100,1):
    if i % 7 == 0 and i % 5 != 0:
        print(f"{i}",end=' ')