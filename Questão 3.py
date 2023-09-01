#importando biblioteca
import math

#entradas
valor_inteiro1 = int(input('Digite o valor do primeiro inteiro: '))
valor_inteiro2 = int(input('Digite o valor do segundo inteiro: '))
valor_real = float(input('Digite o valor do número real: '))

#calculando valores
operacao1 = (2*valor_inteiro1)*(valor_inteiro2/2)
operacao2 = (3*valor_inteiro1)+(valor_real)
operacao3 = pow(valor_real,3)

#imprimindo valores
print('O valor da operação um é {}.'.format(operacao1))
print('O valor da operação dois é {}.'.format(operacao2))
print('O valor da operação três é {}.'.format(operacao3))