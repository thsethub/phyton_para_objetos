import math

#recebendo as entradas
valor_hora = float(input('Escreva quanto você ganha por hora: '))
horas_trabalhadas = float(input('Escreva quantas horas você trabalhou esse mês: '))

#calculando valores
salario_total = (valor_hora*horas_trabalhadas)
valor_INSS = salario_total*(0.08)
valor_sindicato = salario_total*(0.05)
salario_liquido = salario_total-(valor_INSS+valor_sindicato+(salario_total*(0.11)))
descontos = valor_INSS+valor_sindicato+(salario_total*(0.11))

#imprimindo valores
print('__________________________________________________________________')
print('O salário bruto foi R${}'.format(round(salario_total,2)))
print('O valor pago ao INSS foi R${}'.format(round(valor_INSS,2)))
print('O valor pago ao sindicato foi R${}'.format(round(valor_sindicato,2)))
print('O salário líquido foi R${}'.format(round(salario_liquido,2)))
print('O valor total de descontos foi R${}'.format(round(descontos,2)))