import math

def calcular_cdb(valor_investido, taxa_anual, anos):
    montante = valor_investido * (1 + taxa_anual / 100) ** anos
    return montante

def calcular_cdc(valor_emprestado, taxa_mensal, meses):
    taxa_decimal = taxa_mensal / 100
    parcela = valor_emprestado * (taxa_decimal * (1 + taxa_decimal) ** meses) / ((1 + taxa_decimal) ** meses - 1)
    total_pago = parcela * meses
    juros_totais = total_pago - valor_emprestado
    return parcela, total_pago, juros_totais


valor_cdb = float(input("Digite o valor investido no CDB: R$ "))
taxa_cdb = float(input("Digite a taxa de juros anual do CDB (%): "))
ano_vencimento = int(input("Digite o ano de vencimento do CDB: "))
ano_atual = 2025  
anos_cdb = ano_vencimento - ano_atual


montante_cdb = calcular_cdb(valor_cdb, taxa_cdb, anos_cdb)
juros_cdb = montante_cdb - valor_cdb


valor_cdc = valor_cdb  
taxa_cdc = float(input("Digite a taxa de juros mensal do CDC (%): "))
prazo_cdc = int(input("Escolha o prazo do CDC (24, 36 ou 60 meses): "))


parcela_cdc, total_pago_cdc, juros_cdc = calcular_cdc(valor_cdc, taxa_cdc, prazo_cdc)


lucro_banco = juros_cdc - juros_cdb


print("\nRESULTADOS:")
print(f"Montante final do CDB: R$ {montante_cdb:.2f}")
print(f"Juros pagos pelo banco no CDB: R$ {juros_cdb:.2f}")
print(f"Valor das parcelas do CDC: R$ {parcela_cdc:.2f}")
print(f"Montante total pago pelo cliente CDC: R$ {total_pago_cdc:.2f}")
print(f"Juros pagos pelo cliente CDC: R$ {juros_cdc:.2f}")
print(f"Lucro do banco: R$ {lucro_banco:.2f}")
