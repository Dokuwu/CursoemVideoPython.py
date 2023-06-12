from random import choice
from time import sleep
print('Bem vindo ao meu jogo!!! Vamos jogar um classico, pedra papel e tesoura!')
jogador = str(input('Escolha! Pedra, papel ou tesoura? ')).strip().lower()
lista = ['pedra', 'papel', 'tesoura']
pc = choice(lista)
print('\033[1:31m{:^17}\033[m'.format('PEDRA'))
sleep(1)
print('\033[1:31m{:^18}\033[m'.format('PAPEL'))
sleep(1)
print('\033[1:31m{:^22}\033[m'.format('TESOURA!!!'))
sleep(1)
print('\033[1:34m-=\033[m'*15)
print('\033[1:33mComputador jogou {}\033[m'.format(pc.upper()))
print('\033[1:33mJogador jogou {}\033[m'.format(jogador.upper()))
print('\033[1:34m-=\033[m'*15)
sleep(1)
if jogador == 'pedra' and pc == 'tesoura':
    print('Maldito! Venceu...')
elif jogador == 'papel' and pc == 'pedra':
    print('Maldito! Venceu..')
elif jogador == 'tesoura' and pc == 'papel':
    print('Maldito! Venceu...')
elif pc == 'pedra' and jogador == 'tesoura':
    print('Ganhei!!!')
elif pc == 'papel' and jogador == 'pedra':
    print('Ganhei!!!')
elif pc == 'tesoura' and jogador == 'papel':
    print('Ganhei!!!')
elif pc == jogador:
    print('Empatamos!!! Jogamos o mesmo.')
elif jogador == 'mao de deus' or jogador == 'mão de deus':
    print('\033[1:31mISSO É BATOTAAAA!!!!\033[m')
    print('\033[1:31mVAI SER BANIDO DA EXISTENCIA!!!\033[m')
    print('\033[1:31mEM \033[m')
    print('\033[4:32m1!!!\033[m')
    sleep(1)
    print('\033[7:33m2!!!\033[m')
    sleep(1)
    print('\033[0:36m3!!!\033[m')
    sleep(1)
    print('\033[1:37mDead (olavo de carvalho)\033[m')
else:
    print('Você não digitou certo...')
