equipa = ('Palmeiras', 'Fluminense', 'Flamengo', 'Corinthians', 'Athletico-PR', 'Internacional', 'Atlético-MG',
          'América-MG', 'Bragantino', 'Santos', 'Goiás', 'São Paulo', 'Botafogo', 'Ceará', 'Fortaleza',
          'Cuiabá', 'Avaí', 'Coritiba', 'Atlético-GO', 'Juventude')
print('-='*20)
print(f'Lista de equipas do Brasíleirão: {equipa}')
print('-='*20)

#print('Os 5 primeiros são', end=' ')
#for c in range(0,5):
#    print(equipa[c], end=', ')

print('Os 5 primeiros são: ',equipa[0:5])
print('-='*20)

#print('Os 4 ultimos são', end=' ')
#for c in range(1,5):
#    print(equipa[len(equipa)-c], end=', ')

print('Os 4 ultimos são: ',equipa[15:20])
print('-='*20)
print(f'Equipas em ordem alfabética: {sorted(equipa)}')
print('-='*20)
print('O botafogo está na {}ª posição'.format(equipa.index('Botafogo')+1))
print('-='*20)