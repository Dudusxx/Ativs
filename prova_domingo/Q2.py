def main():
    N = int(input("Digite o número de sequências: "))
    
    total_soma = 0        
    total_count = 0       
    menor = None
    maior = None

    for seq in range(1, N + 1):
        print(f"\nSequência {seq}:")
        soma_pares = 0
        while True:
            num = int(input("Digite um número (0 para terminar a sequência): "))
            if num == 0:
                break
            
            if num % 2 == 0:
                soma_pares += num

            
            total_soma += num
            total_count += 1

            
            if menor is None or num < menor:
                menor = num
            if maior is None or num > maior:
                maior = num
        
        print(f"Soma dos números pares da sequência {seq}: {soma_pares}")

    if total_count == 0:
        print("\nNenhum número válido foi digitado.")
    else:
        media = total_soma / total_count
        print(f"\nMédia de todos os números digitados: {media:.2f}")
        print(f"Menor número digitado: {menor}")
        print(f"Maior número digitado: {maior}")

if __name__ == "__main__":
    main()

#essa nao consegui fazer e tiver que ver completa a logica e progressao no gpt