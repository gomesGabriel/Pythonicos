from datetime import date
print('\033[33m-=-\033[m' * 20)
print('\033[33m************* Verifica idade para alistamento *************\033[m')
print('\033[33m-=-\033[m' * 20)
an = int(input('Insira seu ano de nascimento: '))
if (date.today().year - an) == 18:
    print('Esse ano é ano de alistamento {}obrigatório{}.' .format('\033[4;31m', '\033[m'))
elif (date.today().year - an) >= 18:
    print('Já {}passou{} o ano do seu alistamento.' .format('\033[4;31m', '\033[m'))
else:
    print('Você ainda {}não{} precisa se alistar.'.format('\033[4;31m', '\033[m'))
