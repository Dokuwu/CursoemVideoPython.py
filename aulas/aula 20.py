'''
a = 4
b = 5
s = a + b
print(s)

a = 8
b = 9
s = a + b
print(s)

a = 2
b = 1
s = a + b
print(s)
'''

'''
def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma de A + B = {s}')


#Programa Principal
soma(4, 5)
soma(8, 9)
soma(2, 1)
soma(a=4, b=5)
soma(b=4, a=5)
#soma(b=4, 5) vai dar erro
#soma(4, 2, 1) vai dar erro
'''
'''
def contador(*num):
    tam = len(num)
    print(f'Temos ao todo {tam} numeros e são:')
    for valor in num:
        print(f'{valor} ', end='')
    print()


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)
'''
'''
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [7, 2, 5, 0, 4]
print(valores)
dobra(valores)
print(valores)
'''
def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s} ')


soma(5, 2)
soma(2, 9, 4)
