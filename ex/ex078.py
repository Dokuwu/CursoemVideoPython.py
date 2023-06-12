#max min index
numeros = []
for c in range(0,5):
    numeros.append(int(input('Digite o numero na posição {}: '.format(c))))
print('Você digitou... {}'.format(numeros))
print('O menor numero foi {} e está nas posições '.format(min(numeros)), end='')
for l, me in enumerate(numeros):
    if me == min(numeros):
        print(l,end='...')
print('\nO maior numero foi {} e está nas posições '.format(max(numeros)), end='')
for l, ma in enumerate(numeros):
    if ma == max(numeros):
        print(l,end='...')
