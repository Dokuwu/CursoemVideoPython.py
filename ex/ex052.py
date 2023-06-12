n = int(input('Digite um numero inteiro '))
s = 0
for c in range(1, n+1):
    if n % c == 0:
        print('\033[33m', end='')
        s += 1
    else:
        print('\033[31m', end='')
    print(c, end=' ')
if s == 2:
    print(' É primo.')
else:
    print(' Não é primo')