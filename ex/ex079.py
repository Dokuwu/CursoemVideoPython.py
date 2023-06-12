lista = []
q = 'S'
while q == 'S':
    numero = int(input('Digite um numero: '))
    if numero not in lista:
        lista.append(numero)
        print('Valor adicionado com sucesso...')
    else:
        print('VALOR DUPLICADO! Não vou adicionar...')
    while True:
        q = str(input('Deseja continuar ? [S/N] ')).upper().strip()[0]
        if q in 'SN':
            break
lista.sort()
print('Os numeros que digitou em ordem crescente são: ')
print(f'{lista}')