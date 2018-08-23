print('\033[33m-=-\033[m' * 20)
print('\033[33m************* Maior e menor da sequência *************\033[m')
print('\033[33m-=-\033[m' * 20)
maior = 0
menor = 0
for c in range(1, 6):
    p = float(input('Insira o peso da {}ª pessoa: ' .format(c)))
    if c == 1:
        maior = p
        menor = p
    else:
        if p > maior:
            maior = p
        if p < menor:
            menor = p
print('O maior peso lido foi de: {:.2f}kg' .format(maior))
print('O menor peso lido foi de: {:.2f}kg' .format(menor))