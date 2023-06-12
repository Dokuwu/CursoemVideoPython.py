print('='*20)
print('{:^20}'.format('LOJA POUPEIRO'))
print('='*20)
t = menor = maismil = calc = 0
nmenor = ''
while True:
    nome = str(input('Digite o nome do produto: ')).strip().title()
    p = float(input('Preço: R$'))
    calc += 1
    if calc == 1 or p < menor:
        menor = p
        nmenor = nome
    if p > 1000:
        maismil += 1
    t += p
    while True:
        c = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if c in 'SN':
            break
    if c == 'N':
        break
print(f'''O preço total de {calc} produtos é R${t:.2f}.
Teve {maismil} produtos com valor superior a R$1000
O nome do produto mais barato é {nmenor} que custa R${menor:.2f}''')
