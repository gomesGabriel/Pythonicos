print('\033[33m-=-\033[m' * 20)
print('\033[33m{:*^60}\033[m'.format('Simulador de Caixa eletrônico'))
print('\033[33m-=-\033[m' * 20)
print('\033[33m=\033[m' * 40)
print('\033[33m{:^40}\033[m'.format('Banco CEV'))
print('\033[33m=\033[m' * 40)
valor = int(input('Qual volor você quer sacar? R$'))
total = valor
ced = 50
totalCed = 0
while True:
    if total >= ced:
        total -= ced
        totalCed += 1
    else:
        if totalCed > 0:
            print(f'Total de {totalCed} cédulas de RS{ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalCed = 0
        if total == 0:
            break
print('='*50)
print('Volte sempre ao banco CEV! Tenha um bom dia!')
