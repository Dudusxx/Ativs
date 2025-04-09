metros = float(input("digite o valor em metros: "))

km = metros // 1000
m = metros % 1000

print(f"o valor sera de: {km:.2f} km e {m:.2f} mts")