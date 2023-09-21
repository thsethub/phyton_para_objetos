#entradas
temp_C = str(input("Insira a temperatura em graus celsius: "))
var = "°C"

#filtrando °C
for caracter in var:
    temp_C = temp_C.replace(caracter,'')

temp_C = float(temp_C)

#processamento
temp_F = ((temp_C*9)/5) + 32

#saída
print(f"A temperatura {temp_C: .2f}°C em Fahrenheit é {temp_F: .2f}°F.")

