def def_int(s):
    if len(s) == 0:
        return False
    i = 0
    if s[0] == '-':
        if len(s) == 1:
            return False  
        i = 1
    while i < len(s):
        if s[i] < '0' or s[i] > '9':
            return False
        i += 1
    return True

def get_int():
    while True:
        entrada = input("Digite um número inteiro: ")
        if def_int(entrada):
            return int(entrada)
        print("Erro! Digite um número inteiro válido.")

def int_positivo():
    while True:
        entrada = input("Digite um número inteiro positivo: ")
        if def_int(entrada):
            n = int(entrada)
            if n > 0:
                return n
        print("Erro! Digite um número inteiro positivo válido.")

def int_negativo():
    while True:
        entrada = input("Digite um número inteiro negativo: ")
        if def_int(entrada):
            n = int(entrada)
            if n < 0:
                return n
        print("Erro! Digite um número inteiro negativo válido.")

def int_minimo():
    x = get_int()
    while True:
        entrada = input(f"Digite um número inteiro maior ou igual a {x}: ")
        if def_int(entrada):
            n = int(entrada)
            if n >= x:
                return n
        print(f"Erro! Digite um número inteiro maior ou igual a {x}.")

def int_maximo():
    x = get_int()
    while True:
        entrada = input(f"Digite um número inteiro menor ou igual a {x}: ")
        if def_int(entrada):
            n = int(entrada)
            if n <= x:
                return n
        print(f"Erro! Digite um número inteiro menor ou igual a {x}.")

def int_faixa():
    print("Agora vamos definir os limites da faixa:")
    x = get_int()
    y = get_int()
    if x > y:
        x, y = y, x
    while True:
        entrada = input(f"Digite um número inteiro entre {x} e {y}: ")
        if def_int(entrada):
            n = int(entrada)
            if x <= n <= y:
                return n
        print(f"Erro! Digite um número inteiro entre {x} e {y}.")

if __name__ == "__main__":
    print("Teste receber_inteiro():", get_int())
    print("Teste receber_inteiro_positivo():", int_positivo())
    print("Teste receber_inteiro_negativo():", int_negativo())
    print("Teste receber_inteiro_minimo():", int_minimo())
    print("Teste receber_inteiro_maximo():", int_maximo())
    print("Teste receber_inteiro_faixa():", int_faixa())

#usei o gpt para ter uma sintaxe mais coesa e com palavras chaves mais diretas.
