print('<--------Calculo de media ponderada--------->')


nota1 = float(input("Digite a primeira nota:"))
peso1 = int(input('digite o peso 1:'))
nota2 = float(input('digite a nota 2:'))
peso2 = int(input('digite o peso 2:'))
nota3 = float(input('digite a nota 3:'))
peso3 = int(input('digite o peso 3:'))

# calculo

mediaP = (nota1*peso1 + nota2*peso2 + nota3*peso3) / (peso1 + peso2 + peso3)

# saida
print('<------------------->')
print("Sua média será:", mediaP) 