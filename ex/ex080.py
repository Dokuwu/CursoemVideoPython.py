lista = []
p = 0
for c in range(0, 5):
    numero = int(input('Digite um numero: '))
    if c == 0:
        lista.append(numero)
        print('Numero adicionado na posição 0.')
    if c >= 1:
        for d,n in enumerate(lista):
            if numero < n:
                lista.insert(lista.index(n), numero)
                print('Numero adicionado na posição {}.'.format(d))
                break
            if numero > n and (numero < lista[d] or d == len(lista) - 1):
                lista.insert((lista.index(n) + 1), numero)
                print('Numero adicionado na posição {}.'.format(d + 1))
                break
print('Os valores digitados em ordem foram: ', lista)
