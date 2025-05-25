def mdc(a, b):
    
    if b == 0:
        return a
    
    return mdc(b, a % b)


if __name__ == "__main__":
    x = int(input("Digite o primeiro número inteiro positivo: "))
    y = int(input("Digite o segundo número inteiro positivo: "))
    
    if x <= 0 or y <= 0:
        print("Por favor, digite números inteiros positivos.")
    else:
        resultado = mdc(x, y)
        print(f"O MDC de {x} e {y} é {resultado}")
