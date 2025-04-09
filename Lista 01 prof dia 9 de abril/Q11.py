while True:
    try:
        numero = int(input("Digite um número inteiro de 3 dígitos: "))

        if 100 <= numero <= 999:
           
            invertido = int(str(numero)[::-1])
            print(f"O número invertido é: {invertido}")
            break
        else:
            print("Número inválido! Digite um número com exatamente 3 dígitos.\n")

    except ValueError:
        print("Entrada inválida! Digite apenas números inteiros.\n")
