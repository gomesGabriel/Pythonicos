print('\033[33m-=-\033[m' * 20)
print('\033[33m************ Maior, Menor e média em loop ************\033[m')
print('\033[33m-=-\033[m' * 20)
r = 's'
m = s = q = mx = mn = 0
while r in 'Ss':
    num = int(input('Digite um valor: '))
    s += num
    q += 1
    if q == 1:
        mx = mn = num
    else:
        if num > mx:
            mx = num
        if num < mn:
            mn = num
    r = str(input('Quer continuar? [S/N] ')).upper().strip()[0]   ##[0] pega só a primeira coisa digitada
m = s / q
print('Você digitou {} números e a média foi {}' .format(q, m))
print('O maior foi {} e o menor foi {}' .format(mx, mn))
