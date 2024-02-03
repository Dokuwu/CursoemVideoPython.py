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

def resumo(saldo,p1,p2):
    ##poderia criar uma função para formatar texto
    print("=" * 25)
    print(f"{'RESUMO DO VALOR':^25}")
    print("=" * 25)
    print(f"Preço analisado: {moeda(saldo):>{25 - len('Preço analisado: ')}}")
    print(f"Dobro do preço: {dobro(saldo,True):>{25 - len('Dobro do preço: ')}}")
    print(f"Metado do preço: {metade(saldo,True):>{25 - len('Metado do preço: ')}}")
    print(f"{p1} de aumento: {aumentar(saldo,p1,True):>{25 - len(f'{p1} de aumento: ')}}")
    print(f"{p2} de remoção: {diminuir(saldo, p2, True):>{25 - len(f'{p2} de remoção: ')}}")
    print("=" * 25)