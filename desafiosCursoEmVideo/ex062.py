print('\033[33m-=-\033[m' * 20)
print('\033[33m************ Super Progressão aritmética(while) ************\033[m')
print('\033[33m-=-\033[m' * 20)
p = int(input('Insira o primeiro valor de uma PA: '))
r = int(input('Insira a razão da PA: '))
t = p
c = 1
tot = 0
m = 10
while m != 0:
    tot += m
    while c <= tot:
        print('{} →' .format(t), end=' ')
        t += r
        c += 1
    print('Pausa')
    m = int(input('Quantos termos você quer mostrar a mais? '))

print('Fim da PA com {} termos mostrados.' .format(tot))
