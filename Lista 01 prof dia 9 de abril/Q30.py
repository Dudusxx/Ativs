total_minutos = int(input("Digite a quantidade de minutos: "))

dias = total_minutos // 1440
resto = total_minutos % 1440

horas = resto // 60
minutos = resto % 60

print(f"{total_minutos} minutos equivalem a {dias} dia(s), {horas} hora(s) e {minutos} minuto(s)")
