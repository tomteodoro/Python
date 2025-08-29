def media_ponderada(lista_notas, lista_pesos):
    if len(lista_notas) != len(lista_pesos):
        return "Erro: as listas de notas e pesos devem ter o mesmo tamanho."
    soma_dos_produtos = 0
    soma_dos_pesos = 0
    for i in range(len(lista_notas)):
        nota = lista_notas[i]
        peso = lista_pesos[i]
        soma_dos_produtos = soma_dos_produtos + (nota * peso)
        soma_dos_pesos = soma_dos_pesos + peso
    media = soma_dos_produtos / soma_dos_pesos
    return media
