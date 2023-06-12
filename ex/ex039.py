from datetime import date
ano = int(input('Em que ano que nasceu? '))
h = date.today().year
i = h - ano
print('Quem nasceu em {} tem {} anos em {}'.format(ano, i, h))
if i < 18:
    print('Ainda não está na hora de se alistar.')
    f1 = 18 - i
    a1 = h + f1
    if f1 == 1:
        print('Ainda tem {} ano para se alistar.'.format(f1))
    else:
        print('Ainda tem {} anos para se alistar.'.format(f1))
    print('Seu alistamento será em {}.'.format(a1))
elif i == 18:
    print('Está na hora de se alistar soldado!')
elif i > 18:
    print('Já passou do tempo de se alistar, espero que tenha se alistado anteriormente.')
    f2 = i - 18
    a2 = h - f2
    if f2 == 1:
        print('Passou {} ano do prazo.'.format(f2))
    else:
        print('Passaram {} anos do prazo.'.format(f2))
    print('Seu alistamento foi em {}.'.format(a2))