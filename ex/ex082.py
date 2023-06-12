p = 'S'
lista = []
pares = []
impares = list() #a mesma coisa que os outros
while p == 'S':
    numero = int(input('Digite um valor: '))
    lista.append(numero)
    while True:
        p = str(input('Deseja continuar ? [S/N] ')).upper().strip()[0]
        if p in 'SN':
            break
for n in lista:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
print('-='*40)
print('Você digitou estes numeros: ', lista)
if len(pares) == 0:
    print('Não existe pares.')
else:
    print('Os pares foram: ', pares)
if len(impares) == 0:
    print('Não existe impares')
else:
    print('Os impares foram: ', impares)
