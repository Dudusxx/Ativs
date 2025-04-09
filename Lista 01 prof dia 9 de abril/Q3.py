
minutos = int(input('Minutos: '))


horas = minutos // 60
minutos_rest = minutos % 60


print(f'> {minutos}min equivalem a {horas}h{minutos_rest}min')