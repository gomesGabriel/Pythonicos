print('-=-' * 20)
print('ANALISANDO TRIÂNGULOS')
print('-=-' * 20)

n1 = float(input('Insira o primeiro valor: '))
n2 = float(input('Insira o segundo valor: '))
n3 = float(input('Insira o terceiro valor: '))
if n1 < n2+n3 and n2 < n1+n3 and n3 < n1 + n2:
    print('Podem formar triângulos')
else:
    print('Não podem formar triângulos.')