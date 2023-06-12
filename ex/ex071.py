from time import sleep
print('='*30)
print('{:^20}'.format('BANCO MONTEPIO'))
print('='*30)
cin = vin = dez = um = 0
while True:
    valor = int(input('Que valor você quer sacar? R$'))
    while True:
        if valor >= 50:
            valor -= 50
            cin += 1
        else:
            break
    while True:
        if valor >= 20:
            valor -= 20
            vin += 1
        else:
            break
    while True:
        if valor >= 10:
            valor -= 10
            dez += 1
        else:
            break
    while True:
        if valor > 0:
            valor -= 1
            um += 1
        else:
            break
    break
print('='*30)
print(f'''Total de {cin} cédulas de R$50
Total de {vin} cédulas de R$20
Total de {dez} cédulas de R$10
Total de {um} cédulas de R$1''')
print('='*30)
sleep(1)
print('Volte sempre ao BANCO MONTEPIO! Tenha um bom dia!')

'''
print('='*30)
print('{:^20}'.format('BANCO MONTEPIO'))
print('='*30)
valor = int(input('Que valor você quer sacar? R$'))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced +=1
    else:
        if totced > 0:
            print('Total de {} cedulas de R${}'.format(total,ced))
        if ced == 50:
            ced=20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        if total == 0:
            break
print('='*30)
sleep(1)
print('Volte sempre ao BANCO MONTEPIO! Tenha um bom dia!')
print('='*30)
'''