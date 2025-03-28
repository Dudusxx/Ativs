print('<--------utilize apenas multiplos de 10--------->')

din = int(input("digite o valor:"))

cal = din // 50
rest = din % 50
nota10 = rest / 10

print("seu troco sera de :", cal, 'nota(s) de 50', "e", nota10, "nota(s) de 10")