def aplicar_desconto(valor, percentual):
    desconto = valor * (percentual / 100)
    valor_desconto = valor - desconto
    return valor_desconto

preço = float(input("Digite o preço do produto: "))
percentual = float(input("Qual o percentual de desconto para o preço do produto digitado: "))
if percentual <= 0:
    print(f"Percentual inválido! Como não houve desconto, o valor a ser pago pelo produto é R$ {preço:.2f}")
    exit()
else:
    print(f"O valor final a ser pago no produto, após aplicação do desconto, é R$ {aplicar_desconto(preço, percentual):.2f}")