def aumentar(num1, percent,formatado = False):
    if formatado:
        return moeda(num1 + (num1 * (percent/100.0)))
    return num1 + (num1 * (percent/100.0))


def diminuir(num1, percent,formatado = False):
    if formatado:
        return moeda(num1 - (num1 * (percent/100.0)))
    return num1 - (num1 * (percent/100.0))


def dobro(num,formatado = False):
    if formatado:
        return moeda(num * 2)
    return num * 2

def metade(num,formatado = False):
    if formatado:
        return moeda(num/2)
    return num / 2

def moeda(num):
    return f"R${num}"