from random import randint
from time import sleep


def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for c in range(0, 5):
        t = randint(1, 10)
        print(t, end=' ')
        sleep(0.5)
        lista.append(t)
    print('PRONTO!')


def somapar(lista):
    par = 0
    for c in lista:
        if c % 2 == 0:
            par += c
    print(f'Somando os valores pares de {lista}, temos {par}.')


num = []
sorteia(num)
somapar(num)
