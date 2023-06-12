def leiaint(n):
    while True:
        m = input(n)
        if m.isnumeric() is True:
            break
        else:
            print('\033[1;31mERRO! Digite um numero inteiro valido.\033[m')
    return m


n = leiaint('Digite um numero: ')
print(f'Voce acabou de digitar o valor {n}.')
