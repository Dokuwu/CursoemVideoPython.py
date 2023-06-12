from time import sleep


def contagem(a, b, c):
    print('=-' * 25)
    print(f'Contagem de {c} até {b} de {c} em {c}')
    if a < b:
        for d in range(a, b+1, c):
            print(d, end=' ')
            sleep(0.25)
    elif a > b:
        for d in range(a, b-1, -c):
            print(d, end=' ')
            sleep(0.25)
    print()


contagem(1, 10, 1)
contagem(10, 0, 2)
print('=-'*25)
print('Agora é a sua vez de personalizar a contagem!')
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
if p < 0:
    p *= -1
if p == 0:
    p = 1
    print('Valor 0 não é possivel fazer, por isso foi mudado para 1.')
sleep(0.5)
contagem(i, f, p)
