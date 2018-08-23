print('\033[33m-=-\033[m' * 20)
print('\033[33m************* Progressão aritmética(while) *************\033[m')
print('\033[33m-=-\033[m' * 20)
p = int(input('Insira o primeiro valor de uma PA: '))
r = int(input('Insira a razão da PA: '))
t = p
c = 1
while c <= 10:
    print('{} →' .format(t), end=' ')
    t += r
    c += 1
print('Fim')
