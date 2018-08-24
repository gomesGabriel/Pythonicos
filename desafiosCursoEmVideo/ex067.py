print('\033[33m-=-\033[m' * 20)
print('\033[33m************ Tabuada de quantos números você quiser ************\033[m')
print('\033[33m-=-\033[m' * 20)
s = n = c = 0
while True:
    n = int(input('Insira um valor: [valor < 0 para parar] '))
    if n < 0:
        break
    print(f'Tabuada do {n}:')
    while c <= 9:
        print(f'{c} x {n} = {c*n}')
        c += 1
    print('-'*40)
    c = 0
print('Fim')
