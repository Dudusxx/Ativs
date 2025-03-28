print("calculo de desconto")

valor = float(input("insira o valor inicial do produto:"))
desc = float(input("insira o valor do desconto em %:"))

cal = valor * (desc/100)

valorf = valor - cal

print(" o valor final sera de:", f"{valorf:.2f}")