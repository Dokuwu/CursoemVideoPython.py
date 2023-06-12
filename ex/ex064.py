n = c = t = 0
c = int(input('Digite um valor, para parar digite 999: '))
while c != 999:
    t += 1
    n += c
    c = int(input('Digite um valor, para parar digite 999: '))
print('Voce digitou {} numeros e a sua soma é {}.'.format(t, n))
