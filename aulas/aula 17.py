'''num = [2,5,8,1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 0)
num.pop(2, 2)
if 4 in num:
    num.remove(4)
else:
    print('Não achei o numero 4')
print(num)
print(len(num))'''

valores = []
for cont in range(0,5):
    valores.append(int(input('Digite um valor: ')))
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei {v}...')
print('Acabou')

a = [2, 3, 4, 7]
b = a
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')

#VAI LIGAR AS DUAS ENTAO O NUMERO NA POSIÇÃO 2 VAI MUDAR PARA O A E O B

a = [2, 3, 4, 7]
b = a[:]
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')

#ASSIM CRIOU UMA COPIA E JA NAO ESTAO LIGADOS
