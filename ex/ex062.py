n1 = float(input('Digite o primeiro termo: '))
R = float(input('Digite a razão: '))
t = 0
c = 1
p = 1
while c != 0:
    print('{} '.format(n1 + (c - 1) * R), end='- ')
    print('PAUSA')
    c += 1
    t += 1
    if c == 11:
        p = int(input('\nQuantos termos quer ver mais? '))
        p = c + p
        if p == c:
            c = 0
    if c == p:
        p = int(input('\nQuantos termos quer ver mais? '))
        p = c + p
        if p == c:
            c = 0
print('Foram mostrados {} termos.'.format(t))

'''
primeiro = float(input('Primeiro termo: '))
razão = float(input('Razão: '))
c = 1
termo = primeiro
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while c <= total:
        print('{} '.format(termo), end='- ')
        termo += razão
        c += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais')
print('Mostrado {} termos.'.format(total)
'''
