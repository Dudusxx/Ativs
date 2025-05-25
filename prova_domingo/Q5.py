def eh_primo(num):
    if num < 2:
        return False
    i = 2
    while i * i <= num:
        if num % i == 0:
            return False
        i += 1
    return True

def verificar_primos_entre(N, M):
    if N > M:
        N, M = M, N  
    numero = N
    while numero <= M:
        if eh_primo(numero):
            print(f"{numero} é primo")
        else:
            print(f"{numero} não é primo")
        numero += 1


if __name__ == "__main__":
    N = int(input("Digite o valor de N: "))
    M = int(input("Digite o valor de M: "))
    verificar_primos_entre(N, M)

#usei um pedaço do seu codigo do github