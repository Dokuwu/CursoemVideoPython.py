'''
numeros = [[], [], []]
for c in range(0, 10):
    if c < 3:
        n = int(input(f'Digite o valor no lugar [0,{c}]: '))
        numeros[0].append(n)
    elif 3 <= c < 6:
        n = int(input(f'Digite o valor no lugar [1,{c-3}]: '))
        numeros[1].append(n)
    elif 6 <= c < 9:
        n = int(input(f'Digite o valor no lugar [2,{c-6}]: '))
        numeros[2].append(n)
for c in range(0,3):
    print(f'[ {numeros[0][c]} ]', end='')
print('\n', end='')
for c in range(0, 3):
    print(f'[ {numeros[1][c]} ]', end='')
print('\n', end='')
for c in range(0, 3):
    print(f'[ {numeros[2][c]} ]', end='')
print('\n', end='')
'''

matriz = [[0,0,0], [0,0,0], [0,0,0]]
for l in range(0, 3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite o valor no lugar [{l},{c}]: '))
for l in range(0, 3):    
    for c in range(0,3):
        print(f'[ {matriz[l][c]:^6} ]', end='')
    print()
