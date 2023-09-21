#entradas
limite_kg = 50
valor_multa = 4.00

peso = str(input("Insira o peso de peixes em kg: "))
kg = "kg"


if kg in peso:
    for caracter in kg:
        peso = peso.replace(caracter,'')

peso = float(peso)
    
#processamento
if peso > limite_kg:
    excesso = peso - limite_kg
    multa = excesso * valor_multa

    print(f"O valor de multa será R${multa: .2f}")
    print(f"A quantidade de kg foi de {peso: .2f}kg.")

else:
    print(f"O valor do kg não ultrapassou o limite de kg de {limite_kg: .2f}kg, com {peso}0kg.")
