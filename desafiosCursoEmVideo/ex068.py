from random import randint
from time import sleep
print('\033[33m-=-\033[m' * 20)
print('\033[33m************ Jogar Par ou Ímpar ************\033[m')
print('\033[33m-=-\033[m' * 20)
s = n = c = comp = r = 0
while True:
    comp = randint(0, 10)
    n = int(input('Innsira um número: '))
    j = str(input('Você quer par ou ímpar: [P/I] ')).upper().strip()[0]
    s = comp + n
    print('-='*20)
    print(f'Você jogou {n} e o computador escolheu {comp}, e a soma é {s}')
    print('-=' * 20)
    if s % 2 == 0 and j == 'P':
        print('Ganhou')
        print('Vamos jogar novamente...')
        print('-=' * 20, end='\n\n')
        sleep(1)

    if s % 2 > 0 and j == 'I':
        print('Ganhou')
        print('Vamos jogar novamente...')
        print('-=' * 20, end='\n\n')
        sleep(1)

    if s % 2 == 0 and j == 'I':
        print('Perdeu')
        print('-=' * 20)
        sleep(1)
        break

    if s % 2 > 0 and j == 'P':
        print('Perdeu')
        print('-=' * 20)
        sleep(1)
        break
    c += 1
print(f'GAME OVER, você ganhou {c} vezes')
