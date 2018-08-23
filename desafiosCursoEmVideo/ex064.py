print('\033[33m-=-\033[m' * 20)
print('\033[33m************ Tratando valores ************\033[m')
print('\033[33m-=-\033[m' * 20)
num = c = s = 0
num = int(input('Digite um número [999 para parar]:  '))
while num != 999:
    s += num
    c += 1
    num = int(input('Digite um número [999 para parar]:  '))

print('Você digitou {} números e a soma foi {}.' .format(c, s))
