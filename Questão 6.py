#entradas
dia_mes = int(input('Escreva o dia do mês que você irá sair de férias: '))
dia_semana = str(input('Escreva o dia da semana que você irá sair de férias: '))
dias_ferias = int(input('Quantos dias você irá passar de férias?\n'))
print('______________________________________________')
#lógica de desenvolvimento
ferias_total = (dia_mes+dias_ferias)+1

if (ferias_total % 7) == 0:
    dia_atual = 'Domingo'
if (ferias_total % 7) == 1:
    dia_atual = 'Segunda-feira'
if (ferias_total % 7) == 2:
    dia_atual = 'Terça-feira'
if (ferias_total % 7) == 3:
    dia_atual = 'Quarta-feira'
if (ferias_total % 7) == 4:
    dia_atual = 'Quinta-feira'
if (ferias_total % 7) == 5:
    dia_atual = 'Sexta-feira'
if (ferias_total % 7) == 6:
    dia_atual = 'Sábado'

#imprimindo valores
print(f'Você saiu de ferias dia {dia_mes}, {dia_semana}. E voltará de férias depois de {ferias_total} noites, {dia_atual}.')