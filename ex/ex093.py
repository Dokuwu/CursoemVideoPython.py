jogador = dict()
jogador['nome'] = str(input('Nome do jogador: '))
totalpartidas = int(input('Numeros de partidas jogadas: '))
tgolos = 0
lgolos = list()
for c in range(0, totalpartidas):
    lgolos.append(int(input(f'  Quantos golos marcou na partida {c}: ')))
jogador['golos'] = lgolos[:]
jogador['total'] = sum(lgolos)
print('-='*20)
print(jogador)
print('-='*20)
for k,v in jogador.items():
    print(f' - {k} tem o valor {v}')
print('-='*20)
print(f'O jogador {jogador["nome"]} jogou {totalpartidas} partidas.') #ou len(jogador["golos"] no totalpartidas
for i,c in enumerate(lgolos):
    print(f' - Na partida {i}, fez {c} golos.')
print(f'Foi um total de {jogador["total"]} golos.')