while True:
    try:
        num1 = int(input("Digite o primeiro número inteiro: "))
        num2 = int(input("Digite o segundo número inteiro: "))

        if num2 == 0:
            print("O divisor não pode ser zero.\n")
        else:
            quociente = num1 // num2
            resto = num1 % num2

            print(f"Quociente da divisão: {quociente}")
            print(f"Resto da divisão: {resto}")
            break

    except ValueError:
        print("Digite apenas números inteiros.\n")


