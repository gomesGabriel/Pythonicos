s = float(input('Insira seu salário: '))
if s >= 1250:
    print('Seu novo salário é de: R${:.2f}' .format((s*0.1)+s))
else:
    print('Seu novo salário é de: R${:.2f}' .format((s*0.15)+s))
