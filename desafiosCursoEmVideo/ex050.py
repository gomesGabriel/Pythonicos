print('\033[33m-=-\033[m' * 20)
print('\033[33m************* Soma dos pares *************\033[m')
print('\033[33m-=-\033[m' * 20)
s = 0
for c in range(0, 6):
    v = int(input('Insira um valor: '))
    if v % 2 ==0:
        s += v
print('A soma dos números pares digitado é: {}' .format(s))
