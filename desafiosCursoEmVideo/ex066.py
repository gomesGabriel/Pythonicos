print('\033[33m-=-\033[m' * 20)
print('\033[33m************ Soma desconsiderando a Flag ************\033[m')
print('\033[33m-=-\033[m' * 20)
s = n = c = 0
while True:
    n = int(input('Insira um valor: [999 para parar]'))
    if n == 999:
        break
    s += n
    c += 1
print(f'A soma dos {c} valores digitados é: {s}')