n = float(input('Insira quantos km terá sua viagem: '))
if n <= 200:
    print('O preço será de: R${:.2f}' .format(n*0.5))
else:
    print('O preço será de: R${:.2f}' .format(n*0.45))
