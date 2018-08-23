print('\033[33m-=-\033[m' * 20)
print('\033[33m************* Progressão aritmética *************\033[m')
print('\033[33m-=-\033[m' * 20)
p = int(input('Insira o primeiro valor de uma PA: '))
r = int(input('Insira a razão da PA: '))
d = p + (10-1) * r
for c in range(p, d+r, r):
    print('{}'.format(c), end=' →')
print('Fim')