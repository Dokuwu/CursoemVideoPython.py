palavra = 'Perna', 'Sexta', 'Carvalho', 'Ultrakill', 'Gangsta', 'Style', 'Sexy Lady'
for n in palavra:
    print(f'\nNa palavra {n.upper()} as vogais são: ', end='')
    for letra in n:
        if letra in 'AaEeIiOoUu':
            print(f'{letra.lower()} ', end='')