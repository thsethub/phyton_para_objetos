#entradas
valor_salario = float(input('Escreva o valor do salário R$ '))
porcentagem_aumento = str(input('Escreva a porcentagem de aumento: '))
aux1 = '%'

#filtrando o caracter % e convertendo em inteiro
for caracter in aux1:
    porcentagem_aumento = porcentagem_aumento.replace(caracter,'')

porcentagem_aumento = int(porcentagem_aumento)

#calculando valores
valor_aumento = valor_salario*(porcentagem_aumento/100)
salario_aumentado = valor_salario*(porcentagem_aumento/100)+valor_salario

#imprimindo valores
print('_______________________________________')
print(f'O valor de aumento é R${valor_aumento}')
print(f'O salário após o aumento será R${salario_aumentado}')