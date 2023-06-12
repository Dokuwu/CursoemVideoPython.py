a = int(input('Digite um numero. '))
b = int(input('Digite outro numero. '))
c = int(input('Digite outro numero. '))
#verificar quem é menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
print('O menor valor digitado foi {}.'.format(menor))
maior = b
if a > b and a > c:
    maior = a
if c > b and c > a:
    maior = c
print('O menor valor digitado foi {}.'.format(maior))

