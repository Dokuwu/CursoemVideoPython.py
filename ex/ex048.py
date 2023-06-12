s = 0
for c in range(1,501):
    if c % 3 == 0:
        s += c
print('O sumatorio de todos os numeros impares entre 1 e 500, que sao multiplos de 3 é {}.'.format(s))