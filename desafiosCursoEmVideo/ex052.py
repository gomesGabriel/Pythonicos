print('\033[33m-=-\033[m' * 20)
print('\033[33m************* Números primos *************\033[m')
print('\033[33m-=-\033[m' * 20)
n = int(input('Insira um valor: '))
t = 0
for c in range(1, n+1):
    if n % c == 0:
        print('\033[32m', end=' ')
        t += 1
    else:
        print('\033[31m', end=' ')
    print('{}' .format(c), end=' ')
print('\n\033[mO número {} foi divisível {} vezes.' .format(n, t))
if t == 2:
    print('E por isso é primo.')
else:
    print('E por isso não é primo')