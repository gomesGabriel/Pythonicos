from random import randint
from time import sleep

print('\033[33m-=-\033[m' * 20)
print('\033[33m************* Vamos jogar Jokenpô? *************\033[m')
print('\033[33m-=-\033[m' * 20)

'''
c = randint(1, 3)
p = int(input('Escolha {}1{} para pedra, {}2{} para papel e {}3{} para tesoura: '.format('\033[31m', '\033[m', '\033[32m', '\033[m', '\033[34m', '\033[m')))
if p == 1 or p == 2 or p == 3:
    if c == 1:
        print('Minha escolha foi: {}Pedra{}' .format('\033[33m', '\033[m'))
    elif c == 2:
        print('Minha escolha foi: {}Papel{}'.format('\033[33m', '\033[m'))
    elif c == 3:
        print('Minha escolha foi: {}Tesoura{}'.format('\033[33m', '\033[m'))
    if (c == 1 and p == 1) or (c == 2 and p == 2) or (c == 3 and p == 3):
        print('Deu empate...')
    elif (c == 1 and p == 3) or (c == 2 and p == 1) or (c == 3 and p == 2):
        print('Eu ganhei!!!')
    elif (p == 1 and c == 3) or (p == 2 and c == 1) or (p == 3 and c == 2):
        print('Você ganhou.')
else:
    print('Entre com um valor válido.')
'''
############ Outro modo de fazer:
itens = ('Pedra', 'Papel', 'Tesoura')
comp = randint(0, 2)
print('Suas opções:\n'
      '{}[ 0 ]{} para pedra\n'
      '{}[ 1 ]{} para papel\n'
      '{}[ 2 ]{} para tesoura '.format('\033[31m', '\033[m', '\033[32m', '\033[m', '\033[34m', '\033[m'))
j = int(input('Sua jogada: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')

print('\033[31m-=\033[m' * 15)
print('O computador escolheu: {}' .format(itens[comp]))
print('O jogador escolheu: {}' .format(itens[j]))
print('\033[31m-=\033[m' * 15)

if comp == 0: #PEDRA
    if j == 0: #PEDRA
        print('Empate...')
    elif j == 1: #PAPEL
        print('Você ganhou.')
    elif j == 2: #TESOURA
        print('Eu ganhei!')
    else: #inválido
        print('Valor inválido.')
elif comp == 1: #PAPEL
    if j == 0: #PEDRA
        print('Eu ganhei!')
    elif j == 1: #PAPEL
        print('Empate...')
    elif j == 2: #TESOURA
        print('Você ganhou.')
    else: #inválido
        print('Valor inválido')
elif comp == 2: #TESOURA
    if j == 0: #PEDRA
        print('Você ganhou.')
    elif j == 1: #PAPEL
        print('Eu ganhei!')
    elif j == 2: #TESOURA
        print('Empate...')
    else: #inválido
        print('Insira um valor válido')
