from time import sleep
m = 0
n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))
while m != 5:
    m = int(input('[1] somar\n[2] multiplicar\n[3] maior\n[4] novos números\n[5] sair do programa\nQual opção? '))
    if m == 1:
        print('-='*20)
        print('A soma dos valores é {}.'.format(n1 + n2))
        print('-=' * 20)
        sleep(1.5)
    elif m == 2:
        print('-=' * 20)
        print('O valor da multiplicação dos valores é {}.'.format(n1 * n2))
        print('-=' * 20)
        sleep(1.5)
    elif m == 3:
        maior = n1
        if n2 > n1:
            maior = n2
        print('-=' * 20)
        print('O maior valor é {}.'.format(maior))
        print('-=' * 20)
        sleep(1.5)
    elif m == 4:
        print('-=' * 20)
        n1 = float(input('Digite o primeiro valor: '))
        n2 = float(input('Digite o segundo valor: '))
        print('-=' * 20)
    elif m not in [1, 2, 3, 4, 5]:
        print('-=' * 20)
        print('Opção invalida, tente novamente.')
        print('-=' * 20)
print('-=' * 20)
print('Obrigado por usar nossos serviços!!!')