def area(a, b):
    m = a * b
    print(f'A area de um terreno {a}x{b} é {m}m^2')


print('-='*25)
print('     Controle de terrenos')
print('-='*25)
l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
area(l, c)