print('\033[32m-=-\033[m' * 20)
print('\033[32m***************** Aprovador de Empréstimos *****************\033[m')
print('\033[32m-=-\033[m' * 20)
vc = float(input('Inisira o valor da casa: R$'))
s = float(input('Insira seu salário: R$'))
qa = int(input('Insira em quantos anos pretende pagar: '))
vm = vc / (qa * 12)
print('Para pagar uma casa de R${:.2f} em {} anos'.format(vc, qa), end ='')
print(' a prestação será de: R${:.2f}' .format(vm))
if vm <= (s*0.3):
    print('Empréstimo aprovado com sucesso, o valor mensal será de: {}R${:.2f}{}' .format('\033[1;31m', vm, '\033[m'))
else:
    print('Empréstimo negado, o valor da parcela é maior que 30% do seu salário.')
