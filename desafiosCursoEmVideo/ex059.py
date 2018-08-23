from time import sleep
print('\033[33m-=-\033[m' * 20)
print('\033[33m************* Mini calculadora *************\033[m')
print('\033[33m-=-\033[m' * 20)
v1 = float(input('Insira um valor: '))
v2 = float(input('Insira outro valor: '))
l = ['SOMAR', 'MULTIPLICAR', 'MAIOR', 'NOVOS NÚMEROS', 'SAIR DO PROGRAMA']


c = 0
while c != 5:
    if c <= 5:
        print('Suas opções são: \n[1]{}\n[2]{}\n[3]{}\n[4]{}\n[5]{}'.format(l[0], l[1], l[2], l[3], l[4]))
        c = int(input('Insira sua escolha: '))
        print('\033[33m-=-\033[m' * 10)
        if c == 1:
            print('Você escolheu a opção [1]')
            print('A soma é: {}' .format(v1+v2))
            print('\033[33m-=-\033[m' * 10)
            sleep(3)
        elif c == 2:
            print('Você escolheu a opção [2]')
            print('A multiplicação é: {}'.format(v1 * v2))
            print('\033[33m-=-\033[m' * 10)
            sleep(3)
        elif c == 3:
            print('Você escolheu a opção [3]')
            if v1 > v2:
                print('O primeiro valor é maior: {}' .format(v1))
            elif v2 > v1:
                print('O segundo valor é maior: {}'.format(v2))
            else:
                print('Os valores são iguais: {}={}'.format(v1, v2))
            print('\033[33m-=-\033[m' * 10)
            sleep(3)
        elif c == 4:
            print('Você escolheu a opção [4]')
            print('Insira novos valores: ')
            v1 = float(input('Insira um valor: '))
            v2 = float(input('Insira outro valor: '))
            print('\033[33m-=-\033[m' * 10)
            sleep(3)
        print('O que deseja fazer? Suas opções são: \n[1]{}\n[2]{}\n[3]{}\n[4]{}\n[5]{}'.format(l[0], l[1], l[2], l[3], l[4]))
    else:
        print('Insira uma opção válida.')
        print('O que deseja fazer? Suas opções são: \n[1]{}\n[2]{}\n[3]{}\n[4]{}\n[5]{}'.format(l[0], l[1], l[2], l[3],
                                                                                                l[4]))
        print('\033[33m-=-\033[m' * 10)
        sleep(3)
print('\033[33m-=-\033[m' * 10)
print('Você escolheu a opção [5], logo, saiu do programa')