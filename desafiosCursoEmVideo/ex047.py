print('\033[33m-=-\033[m' * 20)
print('\033[33m************* Números pares *************\033[m')
print('\033[33m-=-\033[m' * 20)
for c in range(1, 51):
    if c%2 == 0:
        print(c)
print('Apenas esses são pares entre 1 e 50.')