r1 = float(input('Digite o comprimento da primeira reta. '))
r2 = float(input('Digite o comprimento da segunta reta. '))
r3 = float(input('Digite o comprimento da terceira reta. '))
if r1 + r2 > r3 and r3 + r2 > r1 and r1 + r3 > r2:
    print('Estas retas podem formar um triangulo.')
else:
    print('Não dá para formar um trianglo com estas retas.')