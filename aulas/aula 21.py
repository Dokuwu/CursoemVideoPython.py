def contagem(i, f, p):
    """
    -> Faz uma contagem e mostra na tela
    :param i: inicio da contagem
    :param f: fim da contagem
    :param p: passo de contagem
    :return: sem retorno
    """
    print('=-' * 25)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    if i < f:
        for d in range(i, f + 1, p):
            print(d, end=' ')
    elif i > f:
        for d in range(i, f - 1, -p):
            print(d, end=' ')


help(contagem)


def somar(a=0, b=0, c=0):
    s = a + b + c
    print(s)


somar(3, 2, 5)
somar(8, 4)
somar()


def funcao():
    n1 = 4
    print(f'N1 dentro vale {n1}')


n1 = 2
funcao()
print(f'N1 global vale {n1}')


def somar(a=0, b=0, c=0):
    s = a + b + c
    return s


r1 = somar(2, 2, 3)
r2 = somar(2, 2)
r3 = somar(4)
print(f'Os resultados foram', r1, r2, r3)


def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


n = int(input('Digite um numero: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')

f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2}, {f3}')


def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um numero: '))
if par(num):
    print('É par!')
else:
    print('Não é par')