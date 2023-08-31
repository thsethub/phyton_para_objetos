#entradas
num_dias = int(input("Digite a quantidade de dias: \n"))
num_horas = int(input("Digite a quantidade de horas: \n"))
num_min = int(input("Digite a quantidade de minutos: \n"))
seg = int(input("Digite a quantidade de segundos: \n"))

#calculo das variáveis

num_dias = num_dias*24*60*60
num_horas = num_horas*60*60
num_min = num_min*60

all_seg = num_dias+num_min+num_horas+seg

#imprimindo valores

print('O valor total de segundos é {}.'.format(all_seg))