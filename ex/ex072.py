lista = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze',
         'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezanove', 'Vinte')
n = 'S'
while n == 'S':
    while True:
        numero = int(input('Digite um numero entre 0 e 20: '))
        if 0 <= numero <= 20:
            break
        print('Tente novamente. ', end='')
    print(f'Você digitou o numero {lista[numero]}')
    n = str(input('Quer tentar de novo? [S/N] ')).strip().upper()[0]