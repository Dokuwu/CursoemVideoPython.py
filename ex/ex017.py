a = float(input('Comprimento do cateto oposto: '))
b = float(input('Comprimento do cateto adjacente: '))
print('A hipotnusa vai medir {}'.format((a**2+b**2)**(1/2)))

# ouuuu

from math import pow,sqrt
a = float(input('Comprimento do cateto oposto: '))
b = float(input('Comprimento do cateto adjacente: '))
print('A hipotnusa vai medir {}'.format(sqrt(pow(a,2)+pow(b,2))))

# OUUUUUUUUUUU

from math import hypot

a = float(input('Comprimento do cateto oposto: '))
b = float(input('Comprimento do cateto adjacente: '))
print('A hipotnusa vai medir {}'.format(hypot(a,b)))