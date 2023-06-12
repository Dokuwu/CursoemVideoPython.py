from random import randint
from time import sleep
n = randint(0,5)
print('-=-'*20)
print('Vou pensar em um numero de 0 a 5...')
print('-=-'*20)
a = int(input('Tente adivinhar o numero! '))
print('PROCESSANDO...')
sleep(2)
print('Adivinhou!' if a == n else 'Não conseguiu, eu pensei no {}.'.format(n))