import random
from time import sleep
print('\033[33m-=-\033[m' * 20)
print('\033[33m****Vou pensar em um número entre 0 e 10. Tente advinhar****\033[m')
print('\033[33m-=-\033[m' * 20)
comp = random.randint(0, 10)
jog = int(input('Em que número pensei? '))
print('PROCESSANDO ...')
sleep(2)
cont = 1
while comp != jog:
    print('Não foi dessa vez. Tente novamente.')
    jog = int(input('Em que número pensei? '))
    cont += 1
print('Parabéns você venceu! Foram necessária(s) {} tentativa(s)' .format(cont))
