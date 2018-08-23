print('\033[31m-=-\033[m' * 20)
print('\033[31m*************** Comparador de números ***************\033[m')
print('\033[31m-=-\033[m' * 20)
v = int(input('Insira um valor: '))
v2 = int(input('Insira um segundo valor: '))
if v > v2:
    print('O {}primeiro{} valor é maior.' .format('\033[32m', '\033[m'))
elif v2 > v:
    print('O {}segundo{} valor é maior.' .format('\033[34m', '\033[m'))
else:
    print('Os valores são {}iguais{}' .format('\033[31m', '\033[m'))
