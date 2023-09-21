#entradas
valor_hora = float(input("Insira quanto você ganha por hora: R$"))
horas_trabalhadas = float(input("Insira quantas horas você trabalhou esse mês: "))
print("\n")

#processamento
salario = valor_hora * horas_trabalhadas

#saídas
print(f"O seu salário no final do mês foi de: R${salario: .2f}")