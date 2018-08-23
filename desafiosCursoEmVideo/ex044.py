print('\033[33m-=-\033[m' * 20)
print('\033[33m************* Valor a ser pago *************\033[m')
print('\033[33m-=-\033[m' * 20)
v = float(input('Insira o valor a ser pago: R$'))
c = int(input('Insira a condição de pagamento {}1{} para dinheiro/cheque, {}2{} para à vista no cartão'
              ',{}3{} para até 2x no cartão e {}4{} para 3x ou mais no cartão: ' .format('\033[1;31m', '\033[m', '\033[1;32m', '\033[m', '\033[1;34m', '\033[m',  '\033[1;35m', '\033[m')))
if c == 1:
    print('O valor a ser pago terá 10% de desconto, totalizando em: {}R${}{} no dinheiro/cheque'.format('\033[1;32m', v-(v*0.1),  '\033[m'))
elif c == 2:
    print('O valor a ser pago terá 5% de desconto, totalizando em: {}R${}{} no cartão em até 2x'.format('\033[1;32m', v-(v * 0.05),  '\033[m'))
elif c == 3:
    print('O valor a ser pago será: {}R${}{} no cartão em 3x ou mais' .format('\033[1;32m', v,  '\033[m'))
elif c == 4:
    print('O valor a ser pago terá 20% de juros, totalizando em: {}R${}{} no cartão em 3x ou mais' .format('\033[1;32m', v + (v * 0.2),  '\033[m'))
else:
    print('Entre com uma opção válida.')
