print('\033[33m-=-\033[m' * 20)
print('\033[33m************ Sequência de Fibonacci ************\033[m')
print('\033[33m-=-\033[m' * 20)
i = int(input('Quantos termos para ser mostrados? '))
t1 = 0
t2 = 1
print('{} → {}'.format(t1, t2), end=' ')
c = 3
while c <= i:
    t3 = t1 + t2
    print('→ {}'.format(t3), end=' ')
    t1 = t2
    t2 = t3
    c += 1
print('\nFim')
