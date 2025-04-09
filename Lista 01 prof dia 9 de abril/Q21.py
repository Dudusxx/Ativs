temperatura_f = float(input('Temperatura (F): '))


temperatura_c = (5 * temperatura_f - 160) / 9


resultado = f'Temperatura: {temperatura_f:.2f}F equivalem a {temperatura_c:.2f}C'
print(resultado)