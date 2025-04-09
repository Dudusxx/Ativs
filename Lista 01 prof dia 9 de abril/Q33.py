numero = input("Digite um número inteiro de 3 dígitos: ")

if len(numero) == 3 and numero.isdigit():
    inverso = numero[::-1]  # Inverte a string
    soma = int(numero) + int(inverso)
    print(f"A soma de {numero} com seu inverso {inverso} é: {soma}")
else:
    print("Entrada inválida. Digite exatamente 3 dígitos numéricos.")
