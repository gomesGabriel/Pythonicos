a = int(input('Insira um ano: '))
if a%400==0:
    print('Ano bissexto.')
else:
    if a%4 == 0:
        if a%100 != 0:
            print('Ano bissexto.')
        else:
            print('Não é ano bissexto.')
    else:
        print('Não é ano bissexto.')
