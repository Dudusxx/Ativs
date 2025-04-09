total_horas = int(input("Digite a quantidade de horas: "))

semanas = total_horas // 168
resto_horas = total_horas % 168

dias = resto_horas // 24
horas = resto_horas % 24

print(f"{total_horas} horas equivalem a {semanas} semana(s), {dias} dia(s) e {horas} hora(s)")
