import random
from time import sleep
n = random.randrange(0, 5)
e = int(input('Advinhe o número escolhido, entre 0 e 5: '))
if n == e:
    print('Parabéns você acertou')
else:
    print('Não foi dessa vez')

###################
comp = random.randint(0, 5)
print('-=-' *20)
print('Vou pensar em um número entre 0 e 5. Tente advinhar...')
print('-=-' *20)
jog = int(input('Em que número pensei? '))
print('PROCESSANDO ...')
sleep(2)
if comp == jog:
    print('Parabéns você venceu!')
else:
    print('Não foi dessa vez.')