print('\033[33m-=-\033[m' * 20)
print('\033[33m************* Verifica se são palíndromos *************\033[m')
print('\033[33m-=-\033[m' * 20)
f = str(input('Insira uma frase: ')).strip().upper()
p = f.split()
j = ''.join(p)
'''
i = ''

for l in range(len(j)-1, -1, -1):
    i += j[l]
'''
i = j[::-1]
print('Você digitou {} e o inverso é: {}' .format(j, i))
if j == i:
    print('Logo temos um palíndromo')
else:
    print('Logo não temos um palíndromo')
