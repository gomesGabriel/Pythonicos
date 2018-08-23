from datetime import date
print('\033[33m-=-\033[m' * 20)
print('\033[33m************* Verifica idade para natação *************\033[m')
print('\033[33m-=-\033[m' * 20)
an = int(input('Insira seu ano de nascimento: '))
i = date.today().year - an
if i <= 9:
    print('{}Mirin{}'.format('\033[4;30m', '\033[m'))
elif i > 9 and i <= 14:
    print('{}Infantil{}'.format('\033[4;31m', '\033[m'))
elif i > 14 and i <= 19:
    print('{}Junior{}' .format('\033[4;32m', '\033[m'))
elif i > 19 and i <= 20:
    print('{}Sênior{}' .format('\033[4;33m', '\033[m'))
elif i > 20:
    print('{}Master{}' .format('\033[4;34m', '\033[m'))
