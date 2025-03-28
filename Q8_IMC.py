print("calculo de IMC")
altura = float(input("digite sua altura(m):"))
peso = float(input("digite seu peso(Kg):"))

cal = peso / (altura ** 2)

print("seu imc sera de:" , f"{cal:.2f}")