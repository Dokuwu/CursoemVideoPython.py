print('-='*12)
print('SEQUENCIA DE FIBONACCI')
print('-='*12)
n = int(input('Quantos termos quer mostrar? '))
t1 = 0
t2 = 1
print('~'*33)
print('{} - {}'.format(t1,t2),end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    cont += 1
    print(' - {}'.format(t3), end='')
    t1 = t2
    t2 = t3
print(' - Fim')
print('~'*33)
