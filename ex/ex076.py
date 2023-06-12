print('='*40)
print('{:^40}'.format('LISTA DE PREÇOS'))
print('='*40)
lista = ('Pão', 0.13, 'Cacete', 1, 'Napoleão', 2, 'Pastel de nata', 0.50, 'Coca Cola', 1.50, 'Francesinha', 8,
         'Agua das pedras', 0.7, 'Bacalhau', 24)
for n in range(0,len(lista)):
    if n % 2 == 0:
        print(f'{lista[n]:.<30}',end='')
    else:
        print(f'€{lista[n]:>8.2f}')
print('='*40)
