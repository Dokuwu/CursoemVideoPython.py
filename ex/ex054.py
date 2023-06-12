from datetime import date
h = date.today().year
ma = 0
me = 0
for c in range(1,8):
    n = int(input('Digite a data de nascimento da {}ª pessoa: ').format(c))
    if h-n >= 21:
        ma = ma + 1
    else:
        me = me + 1
print('Tem {} maiores de idade e {} menores de idade.'.format(ma, me))
