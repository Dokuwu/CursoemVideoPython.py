print('Temos uma progressão aritmetrica.')
u1 = float(input('Digite o primeiro termo: '))
R = float(input('Digite a razão: '))
print('Os dez primeiros termos da progressão são:')
for c in range(1,11):
    print('{}'.format(u1 + (c - 1 )*R), end=' - ')
print('ACABOU')
