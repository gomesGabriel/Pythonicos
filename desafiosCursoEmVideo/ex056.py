print('\033[33m-=-\033[m' * 20)
print('\033[33m************* Analisador completo *************\033[m')
print('\033[33m-=-\033[m' * 20)
si = 0
iv = 0
nv = 0
tm = 0
for c in range(1, 4):
    print('---- {}ª Pessoa ----' .format(c))
    n = str(input('Nome: ')).strip()
    i = int(input('Idade: '))
    s = str(input('Sexo [S/M]: ')).strip()
    si += i
    if c == 1 and s in 'Mm':
        iv = i
        nv = n
    if s in 'Mm' and i > id:
        iv = i
        nv = n
    if s in 'Ff' and i < 20:
        tm += 1
print('A média de idade do grupo é: {}' .format(si / 4))
print('O homem mais velho tem {} e se chama: {}' .format(iv, nv))
print('Ao todo são {} mulheres com menos de 20 anos.' .format(tm))

