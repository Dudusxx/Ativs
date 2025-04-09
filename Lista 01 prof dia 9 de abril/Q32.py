
numero = int(input('Número: '))


centena = numero // 100
dezena = (numero % 100) // 10
unidade = (numero % 100) % 10 

inverso = (unidade * 100) + (dezena * 10) + centena

diferenca = numero - inverso 



print(f"{numero} - {inverso} = {diferenca}")