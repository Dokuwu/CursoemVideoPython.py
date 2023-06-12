'''n1 = int(input('Digite um numero para ver o seu fatorial. '))
p = 1
for c in range(1,n1):
    c += 1
    p = p * c
print('O valor de {}! é {}.'.format(n1,p))'''

'''n1 = int(input('Digite um numero para ver o seu fatorial. '))
c = 0
p = 1
while c != n1:
    c += 1
    p = p * c
print('O valor de {}! é {}.'.format(n1, p))'''

'''from math import factorial
n1 = int(input('Digite um numero para ver o seu fatorial. '))
f = factorial(n1)
print(f,' LOL OTARIO TU FEZ AQUILO TUDO.')'''

n1 = int(input('Digite um numero para ver o seu fatorial. '))
c = n1
f = 1
print('Calculando {}! = '.format(n1),end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))