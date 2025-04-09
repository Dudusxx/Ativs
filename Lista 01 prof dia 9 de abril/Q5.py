while True:
    numero = int(input("Digite um número inteiro de 3 dígitos: "))

    if 100 <= numero <= 999:
        c = numero // 100             
        d = (numero % 100) // 10      
        u = numero % 10               

        soma = c + d + u

        print(f"Soma dos dígitos: {c} + {d} + {u} = {soma}")
        break
    else:
        print("Por favor, digite um número com exatamente 3 dígitos.\n")
