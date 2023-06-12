def mai(*num):
    print('=-'*25)
    cont = maior =0
    print('Analisando valores dado...')
    for valor in num:
        print(valor, end=' ')
        if cont == 0:
            maior = valor
            cont += 1
        if valor > maior:
            maior = valor
    print(f'Foram informados {len(num)} valores ao todo')
    print(f'O maior valor informado foi {maior}.')


mai(2, 9, 4, 5, 7, 1)
mai(4, 7, 0)
mai(1, 2)
mai(6)
mai()
