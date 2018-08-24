print('\033[33m-=-\033[m' * 20)
print('\033[33m************ Cadastro de pessoas ************\033[m')
print('\033[33m-=-\033[m' * 20)
maiores18 = homens = mulheresMenos20 = count = countMan = countWoman = 0
while True:
    print('\033[31m-\033[m' * 40)
    print('\033[31mCadastre um pessoa\033[m')
    print('\033[31m-\033[m' * 40)
    idade = int(input('Insira a idade: '))
    sexo = ' '
    while sexo not in 'FM':
        sexo = str(input('Insira o sexo: [F/M]')).upper().strip()[0]

    if idade > 18:
        count += 1
    if sexo == 'M':
        countMan += 1
    if sexo == 'F' and idade < 20:
        countWoman += 1

    controle = ' '
    while controle not in 'SN':
        controle = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    if controle == 'N':
        break

print(f'Ao todo {count} têm mais de 18 anos, foram cadastrados {countMan} homens e {countWoman} mulheres com menos de '
      f'20 anos')
