def calcular_consumo_viagem(distancia_total, perc_eletrico, preco_gasolina, preco_alcool):
    
    consumo_gasolina = (10 + 15) / 2  
    consumo_alcool = consumo_gasolina * 0.8  
    
    
    distancia_eletrico = (perc_eletrico / 100) * distancia_total
    distancia_combustao = distancia_total - distancia_eletrico
    
    
    litros_gasolina = distancia_combustao / consumo_gasolina
    litros_alcool = distancia_combustao / consumo_alcool
    
    
    custo_gasolina = litros_gasolina * preco_gasolina
    custo_alcool = litros_alcool * preco_alcool
    
    return litros_gasolina, custo_gasolina, litros_alcool, custo_alcool


distancia_total = float(input("Digite a distância total da viagem (km): "))
preco_gasolina = float(input("Digite o preço do litro da gasolina (R$): "))
preco_alcool = float(input("Digite o preço do litro do álcool (R$): "))
perc_eletrico = float(input("Digite a porcentagem da viagem que será feita com motor elétrico (%): "))


litros_gasolina, custo_gasolina, litros_alcool, custo_alcool = calcular_consumo_viagem(
    distancia_total, perc_eletrico, preco_gasolina, preco_alcool
)


print("\nResultados da simulação:")
print(f"Se abastecer com gasolina: {litros_gasolina:.2f} litros necessários, custo total R${custo_gasolina:.2f}")
print(f"Se abastecer com álcool: {litros_alcool:.2f} litros necessários, custo total R${custo_alcool:.2f}")
