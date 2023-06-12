jogador = dict()
lista = list()
lgolos = list()
p = 0
while True:
    jogador['nome'] = str(input('Nome do jogador: '))
    totalpartidas = int(input('Numeros de partidas jogadas: '))
    for c in range(0, totalpartidas):
        lgolos.append(int(input(f'  Quantos golos marcou na partida {c}: ')))
    jogador['golos'] = lgolos[:]
    jogador['total'] = sum(lgolos)
    lgolos.clear()
    lista.append(jogador.copy())
    while True:
        r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if r in 'SN':
            break
        print('ERRO! Digite apenas S ou N.')
    if r == 'N':
        break
print('-='*23)
print('{:<4}{:<10}{:<25}{:<5}'.format('cod', 'nome', 'golos', 'total'))
for i, c in enumerate(lista):
    print('{:<4}{:<10}{:<25}{:<5}'.format(i, c["nome"], str(c["golos"]), c["total"]))
'''
print('cod',end='')
for i in jogador.keys()
    print(f'{i:<15}', end='')
print()
for i, c in enumerate(lista):
    print({i:<3}, end=' ')
    for d in c.values():
        print({str(d):<15},end=' ')
    print()
'''
print('-='*23)
while True:
    p = int(input('Mostrar dados de que jogador? [999 para parar] '))
    if p == 999:
        break
    if p >= len(lista):
        print('ERRO! Não existe jogador com codigo {}'.format(p))
    else:
        print(f'<<< LEVANTAMENTO DE DADOS DO JOGADOR {lista[p]["nome"]}:')
        for i, c in enumerate(lista[p]['golos']):
            print(f'    No jogo {i + 1}, fez {c} golos')
    print('-='*23)
print('<<< VOLTE SEMPRE >>>')
