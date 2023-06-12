primeiro = float(input('Primeiro termo: '))
razão = float(input('Razão: '))
c = 1
while c != 11:
    print('{} '.format(primeiro + (c - 1) * razão), end='- ')
    c += 1
print('Acabou')

'''
primeiro = float(input('Primeiro termo: '))
razão = float(input('Razão: '))
c = 1
termo = primeiro
while c <= 10:
    print('{} '.format(termo), end='- ')
    termo += razão
    c += 1
print('Acabou')
'''
