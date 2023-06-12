'''
count = 1
while count <= 10:
    print(count, '... ', end='')
    count += 1
print('Acabou')
'''
'''
count = 1
while true <= 10:
    print(count, '... ', end='')
    count += 1
print('Acabou') VAI FAZER EM UM LOOP INFINITO
'''

n = s = 0
while True:
    n = int(input('Digite um numero: '))
    if n == 999:
        break
    s += n
#print('A soma vale {}'.format(s))
print(f'A soma vale {s}')
