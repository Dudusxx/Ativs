
custo_de_fabrica = float(input('Custo de fábrica:'))
percentual_distribuidor = float(input('Percentual do distribuidor:'))
imposto = float(input('Percentual de impostos:'))


valor_distribuidor = (custo_de_fabrica/100) * percentual_distribuidor
valor_imposto = (custo_de_fabrica/100) * imposto
custo_consumidor = custo_de_fabrica + valor_distribuidor + valor_imposto



print(custo_consumidor)