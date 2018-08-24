from time import sleep
print('\033[33m-=-\033[m' * 20)
print('\033[33m{:*^60}\033[m'.format('Análise preços e produtos'))
print('\033[33m-=-\033[m' * 20)
tot = mais1000 = maisBarato = count = preco = 0
count = 1
nomeBarato = ''
while True:
    print('\033[31m-\033[m' * 40)
    print('{:^50}'.format('\033[31mCadastre um produto\033[m'))
    print('\033[31m-\033[m' * 40)
    preco = int(input('Insira o preço: R$'))
    produto = str(input('Insira o nome do produto: ')).upper().strip()
    controle = str(input('Deseja continuar? [S/N]')).upper().strip()
    sleep(1)
    while controle not in 'SN':
        controle = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
        sleep(1)
    if count == 1 or maisBarato > preco:
        maisBarato = preco
        nomeBarato = produto
        count += 1
    if preco > 1000:
        mais1000 += 1
    tot += preco
    if controle == 'N':
        print('\033[34m-\033[m'*50)
        break
print(f"O total da compra foi: R${tot}\nTemos {mais1000} produtos no valor acima de R$1000\nO produto mais "
      f"barato foi: {nomeBarato}, que custa R${maisBarato}")
print('\033[34m-\033[m' * 50)
