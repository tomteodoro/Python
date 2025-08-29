frase = input("Digite uma frase: ").lower()
qnt = 0

for contador in frase:
    if contador in "aeiou":
        qnt = qnt + 1
    
print(f"Nessa frase existem {qnt} vogal(is)")