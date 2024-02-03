# def fatorial(num):
#     f = 1
#     for c in range(2,num+1):
#         f *= c
#     return f
#
# def dobro(num):
#     return num*2
#
# def triplo(num):
#     return num*3
#import uteis
from util import numeros
num = int(input("Digite valor: "))
# fac = uteis.fatorial(num)
# print(f"O fatorial de {num} é {fac}")
# print(f"O dobro de {num} é {uteis.dobro(num)}")
# print(f"O triplo de {num} é {uteis.triplo(num)}")
fac = numeros.fatorial(num)
print(f"O fatorial de {num} é {fac}")
print(f"O dobro de {num} é {numeros.dobro(num)}")
print(f"O triplo de {num} é {numeros.triplo(num)}")