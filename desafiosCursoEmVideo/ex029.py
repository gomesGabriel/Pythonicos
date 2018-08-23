v = float(input('Qual a velocidade do carro? '))
if v <= 80:
    print('Velocidade ok.')
else:
    print('Sua multa será de: R${:.2f}' .format((v-80)*7))
