numero = input("Digite um número inteiro de 4 dígitos: ")

if len(numero) == 4 and numero.isdigit():
    soma = sum(int(digito) for digito in numero)
    print(f"A soma dos dígitos de {numero} é: {soma}")
else:
    print("Entrada inválida. Digite exatamente 4 dígitos numéricos.")
