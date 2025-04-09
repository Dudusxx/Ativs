print('|>>>>>> Paraíba <<<<<<|')

valor_bem = float(input('Valor do bem R$ :'))


parcela = valor_bem // 3

entrada = (valor_bem % 3) + parcela


print('> Parcelamento: ')
print(f'>> Entrada R$: {entrada:.2f}')
print(f'>> + 2x de R$: {parcela:.2f}')
print('---------------------------')