n1 = float(input('Insira o primeiro valor: '))
n2 = float(input('Insira o segundo valor: '))
n3 = float(input('Insira o terceiro valor: '))
if n1 > n2 and n1 > n3:
    print('O maior é: {:.2f}' .format(n1))
elif n2 > n1 and n2 > n3:
    print('O maior é: {:.2f}'.format(n2))
else:
    print('O maior é: {:.2f}'.format(n3))
if n1 < n2 and n1 < n3:
    print('O menor é: {:.2f}' .format(n1))
elif n2 < n1 and n2 < n3:
    print('O menor é: {:.2f}'.format(n2))
else:
    print('O menor é: {:.2f}'.format(n3))
