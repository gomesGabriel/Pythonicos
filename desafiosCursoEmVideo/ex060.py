print('\033[33m-=-\033[m' * 20)
print('\033[33m************* Fatorial *************\033[m')
print('\033[33m-=-\033[m' * 20)
v = float(input('Insira um valor: '))
c = 1
f = 1
while c <= v:
    f = f * c
    c += 1
print('O fatorial de {} é {}' .format(v, f))