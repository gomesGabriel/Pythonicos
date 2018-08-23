print('\033[33m-=-\033[m' * 20)
print('\033[33m************* Analisando triângulos *************\033[m')
print('\033[33m-=-\033[m' * 20)

n1 = float(input('Insira o primeiro valor: '))
n2 = float(input('Insira o segundo valor: '))
n3 = float(input('Insira o terceiro valor: '))
if n1 < n2+n3 and n2 < n1+n3 and n3 < n1 + n2:
    a = 1
else:
    a = 0
if a == 1:
    if n1 == n2 and n1 == n3:
        print('Podem formar um triângulo {}equilátero{}' .format('\033[4;30m', '\033[m'))
    elif n1 == n2 or n1 == n3 or n2 == n3:
        print('Podem formar um triângulo {}isósceles{}'.format('\033[4;31m', '\033[m'))
    else:
        print('Podem formar um triângulo {}escaleno{}'.format('\033[4;32m', '\033[m'))
else:
    print('Não podem formar triângulos.')
