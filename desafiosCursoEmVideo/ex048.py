print('\033[33m-=-\033[m' * 20)
print('\033[33m************* Soma dos ímpares entre 1 e 500 *************\033[m')
print('\033[33m-=-\033[m' * 20)

s = 0
for c in range(1, 501):
    if c % 2 == 1 and c % 3 == 0:
        s += c
print('A soma dos ímpares múltiplos de 3 é: {}' .format(s))
