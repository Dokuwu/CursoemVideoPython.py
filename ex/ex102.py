def fatorial(n, show=False):
    """
    ---> Calcula o fatorial de um numero
    :param n: O numero a ser calculado
    :param show: (opcional) Mostrar ou nao a conta
    :return: O valor do fatorial do n
    """
    from math import factorial
    f = factorial(n)
    if show is True:
        print(f'{n}', end='')
        for c in range(n - 1, 0, -1):
            print(f' x {c}', end='')
        print(f' = ',end='')
        return f
    else:
        return f


print(fatorial(5,show=True))
