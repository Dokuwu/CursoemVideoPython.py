from random import randint
pc = randint(0, 10)
print('Bem vindo a segunda versão do jogo de adivinhação.')
print('Desta vez poderá digitar quantos numeros quiser até adivinhar.')
jogador = 11
tentativas = 0
while jogador != pc:
    jogador = int(input('Digite um numero entre 0 e 10: '))
    tentativas += 1
    if jogador > pc:
        print('Menos, tente de novo.')
    elif jogador < pc:
        print('Mais, tente de novo.')
print('Parabens!!! Acertou, o numero era {} e levou {} tentativas para acertar.'.format(pc, tentativas))

'''
from random import randint
pc = randint(0, 10)
print('Bem vindo a segunda versão do jogo de adivinhação.')
print('Desta vez poderá digitar quantos numeros quiser até adivinhar.')
acertou = False
tentativas = 0
while not acertou:
    jogador = int(input('Digite um numero entre 0 e 10: '))
    tentativas += 1
    if jogador > pc:
        print('Menos, tente de novo.')
    elif jogador < pc:
        print('Mais, tente de novo.')
    else:
        acertou = True
print('Parabens!!! Acertou, o numero era {} e levou {} tentativas para acertar.'.format(pc, tentativas))
'''
