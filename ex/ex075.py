'''par = ''
tupla = ''
for c in range(0,4):
    n = int(input('Digite um valor '))
    nint = str(n)
    if n % 2 == 0:
        par += nint + ' '
    tupla += nint
print('Apareceu {} vezes o 9.'.format(tupla.count('9')))
if tupla.find('3') > 0:
    print('O 3 está na posição {}.'.format(tupla.find('3')+1))
print('O 3 não foi digitado')
print('Os numeros {} são pares.'.format(par))'''

num = (int(input('Digite um numero: ')), int(input('Digite outro numero: '))
       , int(input('Digite o penultimo numero: ')), int(input('Digite o ultimo numero: ')))
print('Você digitou os numeros: {}'.format(num))
print(f'O numero 9 aparece {num.count(9)} vezes')
if 3 in num:
    print('O numero 3 está na posição {}.'.format(num.index(3) + 1))
else:
    print('O numero 3 não foi digitado.')
print('Os numeros pares foram: ', end='')
for n in num:
    if n % 2 == 0:
        print(f'{n} ', end='')

