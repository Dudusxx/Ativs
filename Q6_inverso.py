print('<----------------->')

numero = int(input("digite um numero:"))

centena = numero // 100
dezena = (numero % 100) // 10
unidade = (numero % 100) % 10 

inverso = (unidade * 100) + (dezena * 10) + centena

print("o inverso do numero escolhido é:", inverso)
