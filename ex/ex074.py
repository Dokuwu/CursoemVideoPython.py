from random import randint
'''tupla = ''
for c in range(0,5):
    numero = randint(0,10)
    if c == 0:
        menor = numero
        maior = numero
    if numero < menor:
        menor = numero
    elif numero > maior:
        maior = numero
    ajuda = str(numero)
    tupla += ajuda + ' '
print('Os numero gerados foram:',tupla)
print(f'O maior foi {maior} e o menor {menor}.')'''
numeros = (randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10), )
print('os numeros criados foram: ',end= '')
for n in numeros:
    print(f'{n} ', end='')
print('\nO maior valor sorteado foi {}'.format(max(numeros)))
print('O menor valor sorteado foi {}'.format(min(numeros)))