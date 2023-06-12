'''
numeros = [[], [], []]
t = 0
for c in range(0, 10):
    if c < 3:
        n = int(input(f'Digite o valor no lugar [0,{c}]: '))
        numeros[0].append(n)
        if n % 2 == 0:
            t += s
    elif 3 <= c < 6:
        n = int(input(f'Digite o valor no lugar [1,{c-3}]: '))
        numeros[1].append(n)
        if n % 2 == 0:
            t += s
    elif 6 <= c < 9:
        n = int(input(f'Digite o valor no lugar [2,{c-6}]: '))
        numeros[2].append(n)
        if n % 2 == 0:
            t += s
for c in range(0,3):
    print(f'[ {numeros[0][c]} ]', end='')
print('\n', end='')
for c in range(0, 3):
    print(f'[ {numeros[1][c]} ]', end='')
print('\n', end='')
for c in range(0, 3):
    print(f'[ {numeros[2][c]} ]', end='')
print(f'A soma de todos os pares é {t}')
print(f'A soma dos numeros da terceira coluna é {numeros[0][2] + numeros[1][2] + numeros[2][2]}')
print(f'A soma dos numeros da segunda linha é {numeros[1][0] + numeros[1][1] + numeros[1][2]}')
'''

matriz = [[0,0,0], [0,0,0], [0,0,0]]
spar = mai = scol = 0
for l in range(0, 3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite o valor no lugar [{l},{c}]: '))
for l in range(0, 3):
    for c in range(0,3):
        print(f'[ {matriz[l][c]:^6} ]', end='')
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
    print()
print(f'A soma de todos os pares é {spar}')
for l in range(0,3):
    scol += matriz[l][2]
print(f'A soma dos numeros da terceira coluna é {scol}')
for l in range(0,3):
    if l == 0:
        mai == matriz[1][l]
    elif matriz[1][c] > mai:
        mai == matriz[1][l]
print(f'A soma dos numeros da segunda linha é {mai}')