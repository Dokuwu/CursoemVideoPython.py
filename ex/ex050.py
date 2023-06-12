s = 0
for c in range(0,6):
    n = int(input('Digite o {} numero: '.format(c)))
    if n % 2 == 0:
        s += n
print('A soma de todos os numeros pares que digitou é {}.'.format(s))