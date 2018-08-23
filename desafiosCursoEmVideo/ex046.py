from time import sleep
from emoji import emojize

print('\033[33m-=-\033[m' * 20)
print('\033[33m************* Contagem regressiva! *************\033[m')
print('\033[33m-=-\033[m' * 20)
for c in range(10, -1, -1):
    print('{}!' .format(c))
    sleep(1)
print(emojize(':fireworks: :fire: ' *5))
