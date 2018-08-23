print('\033[33m-=-\033[m' * 20)
print('\033[33m************* Outra tabuada *************\033[m')
print('\033[33m-=-\033[m' * 20)
v = int(input('Insira um valor: '))
print('A tabuada do {} é: ' .format(v))
for c in range(0, 10):
    print('{} * {} = {}' .format(c, v, c*v))
print('Fim')
