seg = int(input("digite a quantidade de segundos: "))

h = seg // 3600
m = (seg % 3600) // 60
s = (seg % 3600) % 60

print(f"voce tera {h} horas, {m} minutos, {s} segundos")