import math
print('<----------------->')

area = float(input("digite a area a ser pintada em metros quadrados(m²):"))
lata = float(input("digite o rendimento de cada lata de tinta:"))

resp = math.ceil(area / lata)
print("a quantidade de latas sera de :", resp)