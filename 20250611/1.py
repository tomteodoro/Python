dicionario = {
    "maçã": "apple",
    "cachorro": "dog",
    "gato": "cat",
    "livro": "book",
    "água": "water"
}

palavra = input("Digite uma palavra em português para traduzir: ").lower()

if palavra in dicionario:
    print(f"A tradução de '{palavra}' é '{dicionario[palavra]}'")
else:
    print("Palavra não encontrada no dicionário.")
