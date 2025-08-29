letra = input("Digite uma letra: ").lower()

if letra in "aeiou":
    print(f"A letra digitada ({letra}) é uma vogal!")
elif letra in "bcdfghjklmnpqrstvwxyz":
    print(f"A letra digitada ({letra}) é uma consoante!")
else:
    print(f"A letra digitada ({letra}) é um símbolo!")