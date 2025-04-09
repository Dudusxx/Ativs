
salario = float(input('Salário: '))


aumento = salario * (25/100)
novo_salario = salario + aumento 


print(f'Seu salário era R$ {salario:.2f}')
print(f'E aumentará 25%, ou seja, R$ {aumento:.2f}')
print(f'Então, seu novo salário será de R$ {novo_salario:.2f}')