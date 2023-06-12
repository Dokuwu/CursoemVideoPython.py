a = float(input('Digite o seu primeiro numero. '))
b = float(input('Digite o seu segundo numero. '))
if a > b:
    print('O numero {} é maior que {}.'.format(a,b))
elif b > a:
    print('O numero {} é maior que {}.'.format(b,a))
elif a == b:
    print('Não existe maior, pois os dois são iguais.')
