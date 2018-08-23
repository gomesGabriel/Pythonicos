print('\033[33m-=-\033[m' * 20)
print('\033[33m************* Loop se digitado errado *************\033[m')
print('\033[33m-=-\033[m' * 20)
s = str(input('Insira seu sexo: [F/M]')).strip().upper()
a = 0
while a == 0:
    if s == 'F' or s == 'M':
        a = 1
    else:
        print('Valor inválido, insira novamente.')
        s = str(input('Insira um valor válido: [F/M]')).strip().upper()
print('Fim')
