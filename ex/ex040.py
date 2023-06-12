n1 = int(input('A primeira nota: '))
n2 = int(input('A segunda nota: '))
m = (n1 + n2) / 2
print('A sua média é {}.'.format(m))
if m < 5:
    print('Más noticias ... Você reprovou...')
elif 5 <= m < 7:
    print('Vai ter que ir para a recuperação.')
elif m >= 7:
    print('Parabens!!! Você passou.')
