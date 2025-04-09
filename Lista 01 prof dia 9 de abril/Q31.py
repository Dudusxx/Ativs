binario = input("Digite um número binário de 4 dígitos: ")

# Verifica se tem exatamente 4 dígitos e só contém 0 ou 1
if len(binario) == 4 and all(d in '01' for d in binario):
    decimal = int(binario, 2)
    print(f"O número binário {binario} em decimal é: {decimal}")
else:
    print("Entrada inválida. Digite exatamente 4 dígitos binários (0 ou 1).")
