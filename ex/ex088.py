'''
from random import randint
from time import sleep
print('-='*20)
print('{:^30}'.format('Jogo da MEGA SENA'))
print('-='*20)
jogos = []
numeros = []
ciclo = j = 0
t = 99
while j < t:
    t = int(input('Quantos jogos quer sortear? '))
    for c in range(0, t):
        while True:
            num = randint(1,60)
            if num not in lista:
                jogos.append(num)
                ciclo += 1
            if ciclo >= 6:
                ciclo = 0
                break
        jogos.sort()
        numeros.append(jogos[:])
        jogos.clear()
        print(f'Jogo {j+1}º: {numeros[j]}')
        sleep(1)
        j += 1
print('-='* 7,'{:^10}'.format('< BOA SORTE >'),'-='* 7)
'''
from random import randint
from time import sleep
lista = list()
jogos = list()
print('-='*20)
print('{:^30}'.format('Jogo da MEGA SENA'))
print('-='*20)
quant = int(input('Quantos jogos voce quer que eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(0,60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    tot += 1
for i, l in enumerate(jogos):
    print(f'Jogo {i + 1}: {l}')
    sleep(1)
print('-='* 7,'{:^10}'.format('< BOA SORTE >'),'-='* 7)