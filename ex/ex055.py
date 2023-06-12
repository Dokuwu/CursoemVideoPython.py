maior = 0
menor = 0
for c in range(1,6):
    p = float(input('Digite o pesso da {}ª pessoa.'.format(c)))
    if c == 1:
        maior = p
        menor = p
    else:
        if p > maior:
            maior = p
        if p < menor:
            menor = p
print('O maior peso é {} e o menor {}.'.format(maior, menor))