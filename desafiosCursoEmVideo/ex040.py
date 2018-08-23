print('\033[33m-=-\033[m' * 20)
print('\033[33m************* Verifica aprovação *************\033[m')
print('\033[33m-=-\033[m' * 20)
v1 = float(input('Insira sua 1ª nota: '))
v2 = float(input('Insira sua 2ª nota: '))
if ((v1+v2)/2)<= 5:
    print('{}Reprovado{}' .format('\033[4;31m', '\033[m'))
elif ((v1+v2)/2) >= 7:
    print('{}Aprovado{}' .format('\033[4;32m', '\033[m'))
else:
    print('{}Recuperação{}'.format('\033[4;33m', '\033[m'))
