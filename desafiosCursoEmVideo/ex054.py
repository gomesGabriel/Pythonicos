from datetime import date
print('\033[33m-=-\033[m' * 20)
print('\033[33m************* Verifica os maiores de idade *************\033[m')
print('\033[33m-=-\033[m' * 20)
a = date.today().year
tm = 0
tn = 0
for c in range(1, 8):
    n = int(input('Insira o ano de nascimento da {}ª pessoa: '.format(c)))
    i = a - n
    if i >= 21:
        tm += 1
    else:
        tn += 1
print('Ao todo, {} são maiores de idade.' .format(tm))
print('Ao todo, {} são menores de idade.' .format(tn))
