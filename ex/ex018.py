from math import sin,cos,tan,radians
a = float(input('Digite o angulo em graus: '))
print('O seno será {:.3f}\n O cosseno será {:.3f}\n A tangente será{:.3f}'.format(sin(radians(a)),cos(radians(a)),tan(radians(a))))