def fatura(valor_fatura, pagamento, meses):
    juros_rotativo = 0.12  
    multa_atraso = 0.02  
    juros_mora = 0.01  
    
    saldo_devedor = valor_fatura - pagamento
    if saldo_devedor <= 0:
        return pagamento, 0, 0  
    
    for _ in range(meses):
        saldo_devedor *= (1 + juros_rotativo + multa_atraso + juros_mora)
    
    crescimento_percentual = ((saldo_devedor - (valor_fatura - pagamento)) / (valor_fatura - pagamento)) * 100
    
    return saldo_devedor, crescimento_percentual, meses


valor_fatura = float(input("Digite o valor total da fatura: "))
p1 = float(input("Digite o valor do primeiro pagamento (P1): "))
p2 = float(input("Digite o valor do segundo pagamento (P2): "))
meses_p1 = int(input("Quantos meses sem pagar após o primeiro pagamento? "))
meses_p2 = int(input("Quantos meses sem pagar após o segundo pagamento? "))


saldo_p1, crescimento_p1, _ = fatura(valor_fatura, p1, meses_p1)
saldo_p2, crescimento_p2, _ = fatura(valor_fatura, p2, meses_p2)


print("\nResultados da simulação:")
print(f"Cenário 1 (Pagamento P1 = R${p1}, atraso de {meses_p1} meses):")
print(f"  - Saldo final da dívida: R${saldo_p1:.2f}")
print(f"  - Crescimento da dívida: {crescimento_p1:.2f}%")

print(f"Cenário 2 (Pagamento P2 = R${p2}, atraso de {meses_p2} meses):")
print(f"  - Saldo final da dívida: R${saldo_p2:.2f}")
print(f"  - Crescimento da dívida: {crescimento_p2:.2f}%")
