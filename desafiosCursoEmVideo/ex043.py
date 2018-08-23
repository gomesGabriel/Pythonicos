print('\033[33m-=-\033[m' * 20)
print('\033[33m************* Calculadora de IMC *************\033[m')
print('\033[33m-=-\033[m' * 20)
h = float(input('Insira sua altura: (ex.: 1.57) '))
p = float(input('Insira seu peso: (ex.: 90.7) '))
imc = p / pow(h, 2)
if imc <= 18.5:
    print('{}Abaixo{} do peso ideal' .format('\033[4;30m', '\033[m'))
elif imc > 18.5 and imc <= 25:
    print('Peso {}ideal{}' .format('\033[4;31m', '\033[m'))
elif imc > 25 and imc <= 30:
    print('{}Acima{} do peso' .format('\033[4;32m', '\033[m'))
else:
    print('Obesidade {}mórbida{}' .format('\033[4;33m', '\033[m'))
