#definindo constante
salario_imposto = 1200

#recebendo as entradas
salario_total = float(input('Digite o seu salário total: '))

#lógica de imposto de renda
if salario_total > salario_imposto:
    print('Você terá que pagar imposto, pois você recebe mais do que R${}.'.format(salario_imposto))
else:
    print('Você não precisará pagar imposto de renda, pois seu salário é menor ou igual a R${}.'.format(salario_imposto))