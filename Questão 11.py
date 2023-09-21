#entradas
temp_F = float(input("Insira a temperatura em Fahrenheit: "))

#processamento
temp_C = 5 * ((temp_F-32)/9)

#saídas
print(f"A temperatura {temp_F: .2f}°F em celsius é {temp_C: .2f}°C.")