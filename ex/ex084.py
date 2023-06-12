resposta = list()
dados = list()
while True:
    resposta.append(str(input('Nome: ')))
    resposta.append(int(input('Peso: ')))
    dados.append(resposta[:])
    resposta.clear()
    r = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    if r in 'Nn':
        break
maior = list()
menor = list()
for p,i in enumerate(dados):
    if p == 0:
        maior.append(i)
        menor.append(i)
    elif p >= 1:
        if i[1] == maior[0][1]:
            maior.append(i)
        elif i[1] == menor[0][1]:
            menor.append(i)
        elif i[1] > maior[0][1]:
            maior.clear()
            maior.append(i)
        elif i[1] < menor[0][1]:
            menor.clear()
            menor.append(i)
print(f'Ao todo você cadastrou {len(dados)} pessoas.')
print(f'O maior peso foi de {maior[0][1]}kg. Peso de ',end='')
for p in maior:
    print(f'{p[0::2]}',end='')
print(f'\nO menor peso foi de {menor[0][1]}kg.Peso de ',end='')
for p in menor:
    print(f'{p[0::2]}',end='')

'''
temp = []
princ = []
maior = menor = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(int(input('Peso: ')))
    if len(princ) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    princ.append(temp[:])
    temp.clear()
    r = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    if r in 'Nn':
        break
print(f'Ao todo você cadastrou {len(dados)} pessoas.')
print(f'O maior peso foi de {maior}kg. Peso de ',end='')
for p in princ:
    if p[1] == maior:
        print(f'{p[0]}', end='')
print(f'\nO menor peso foi de {menor}kg.Peso de ',end='')
for p in princ:
    if p[1] == menor:
        print(f'{p[0]}', end='')
'''