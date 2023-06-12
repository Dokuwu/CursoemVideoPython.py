h = bd = m = 0
while True:
    print('='*20)
    print('{:^20}'.format('CASDATRE UMA PESSOA'))
    print('=' * 20)
    i = int(input('Idade: '))
    if i > 18:
        m += 1
    while True:
        s = str(input('Sexo: [M/F] ')).strip().upper()[0]
        if s == 'M':
            h += 1
            break
        elif s in 'F':
            if i < 20:
                bd += 1
                break
            else:
                break
    print('=' * 20)
    while True:
        c = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if c in 'SN':
            break
    if c == 'N':
        print('=' * 20)
        break
print(f'''Total de pessoas com mais de 18 anos: {m}
Ao todo temos {h} homens. 
homens cadastrados. E temos {bd} mulheres com menos de 20 anos''')

'''tot18 = totH = totM20 = 0
while True:
    print('=' * 20)
    print('{:^20}'.format('CASDATRE UMA PESSOA'))
    print('=' * 20)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo no in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
        if idade >= 18:
            tot18 += 1
        if sexo == 'M':
            totH += 1
        if sexo == 'F' and idade < 20:
            totM20 += 1
        resp = ' '
        while resp not in 'SN':
            resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resp =='N':
            print('=' * 20)
            break
print(f'Total de pessoas com mais de 18 anos: {tot18}
Ao todo temos {totH} homens.
homens cadastrados. E temos {totM20} mulheres com menos de 20 anos')
'''