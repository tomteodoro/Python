def contar_vogais(texto):
    vogais = "aeiou"
    contador = 0
    for letra in texto:
        if letra in vogais:
            contador += 1
    return contador

frase = input("Digite uma frase para contarmos quantas vogais ela possui: ").lower()
print(f"A frase digitada possui {contar_vogais(frase)} vogal(is)")