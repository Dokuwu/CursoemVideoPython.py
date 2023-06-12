from time import sleep
c = ('\033[m',         #0 - sem cor
     '\033[0;30;41m',  #1 - vermelho
     '\033[0;30;42m',  #0 - verde
     '\033[0;30;43m',  #0 - amarelo
     '\033[0;30;44m',  #0 - azul
     '\033[0;30;45m',  #0 - roxo
     '\033[7;30m'      #0 - branco
     )


def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(1)


def titulo(msg, cor=0):
    sleep(0.75)
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')


comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO!', 1)
