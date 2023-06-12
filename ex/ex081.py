p = 'S'
lista = []
while p == 'S':
    numero = int(input('Digite um valor: '))
    lista.append(numero)
    while True:
        p = str(input('Deseja continuar ? [S/N] ')).upper().strip()[0]
        if p in 'SN':
            break
lista.sort(reverse=True)
print(f'Você digitou ao todo {len(lista)} numeros.')
print(f'Os valores digitados na ordem decrescente são: \n{lista}')
if 5 in lista:
    print('O 5 está presente na lista.')
else:
    print('O 5 não está presente na lista.')