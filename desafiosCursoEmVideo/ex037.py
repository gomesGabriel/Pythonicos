print('\033[31m-=-\033[m' * 20)
print('\033[31m*************** Conversor de bases numéricas ***************\033[m')
print('\033[31m-=-\033[m' * 20)
n = int(input('Insira o valor: '))
t = int(input('Insira {}1{} para binário, {}2{} para octal e {}3{} para hexadecimal: '.format('\033[31m', '\033[m', '\033[32m', '\033[m', '\033[34m', '\033[m')))
if t == 1:
    print('O valor convertido para {}binário{} é: {}{}{}' .format('\033[4;31m', '\033[m', '\033[31m', bin(n)[2:], '\033[m'))
elif t == 2:
    print('O valor convertido para {}octal{} é: {}{}{}' .format('\033[4;33m', '\033[m', '\033[33m', oct(n)[2:], '\033[m'))
elif t == 3:
    print('O valor convertido para {}hexadecimal{} é: {}{}{}' .format('\033[4;34m', '\033[m', '\033[34m', hex(n)[2:], '\033[m'))
else:
    print('Favor inserir um valor válido para a conversão.')