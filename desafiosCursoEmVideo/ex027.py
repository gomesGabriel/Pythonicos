n = str(input('Insira seu nome: ')).strip()
nm = n.split()
print('Primeiro nome é: {}' .format(nm[0]))
print('Último nome é: {}' .format(nm[len(nm)-1]))
