n = int(input('De que numero quer fazer a tabuada? '))
print('='*12)
for c in range(1,11):
    print('{:<2} X {:2} = {}'.format(n , c, n * c))
print('='*12)