def converter_celsius_para_fahrenheit(temp):
    fahrenheit = temp * 1.8 + 32
    return fahrenheit

temperatura = float(input("Digite a temperatura em Celsius: "))
print(f"A temperatura convertida para Fahrenheit é {converter_celsius_para_fahrenheit(temperatura)}")
