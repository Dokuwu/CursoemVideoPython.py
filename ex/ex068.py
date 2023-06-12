from random import randint
print('=-'*15)
print('VAMOS JOGAR PAR OU IMPAR')
print('=-'*15)
cont = 0

while True:
    jogador = int(input('Diga um valor: '))
    PI = ' '
    while PI not in 'PI':
        PI = str(input('Par ou Impar? [P/I] ')).strip().upper()[0]
    pc = randint(0,10)
    if (pc + jogador) % 2 == 0:
        r = 'P'
        d = 'PAR'
    else:
        r = 'I'
        d = 'IMPAR'
    print(f'Você jogou {jogador} e o computador {pc}. Total deu {pc + jogador} DEU {d}')
    print('=-' * 15)
    if PI == r:
        print('Você venceu...\nVamos jogar novamente...')
        cont += 1
        print('=-' * 15)
    else:
        print('Você PERDEU!')
        print('=-' * 15)
        break

if cont == 1:
    print(f'GAME OVER! Você venceu {cont} vez.')
else:
    print(f'GAME OVER! Você venceu {cont} vez.')

