print("<-----------calculo de juros----------->")

capital = float(input("insira o valor inicial a ser aplicado: "))
taxa = float(input("insira a taxa de juros: "))
tempo = int(input("insira a quantidade de tempo(em meses): "))

cal = capital * taxa * tempo

montante = cal + capital

print("o valor do montante com juros aplicado será de: ", f"{montante:.2f}")