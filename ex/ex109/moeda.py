def aumentar(num1, percent, tipoMoeda='R$', formatado=False):
    '''
    --> Calcula o saldo perante um aumento de uma certa percentagem
    :param num1: saldo
    :param percent: percentagem a aumentar
    :param tipoMoeda: o simbolo da moeda por default é R$
    :param formatado: formatar o valor com o simbolo for defaul é False
    :return: valor ou valor formatado
    '''
    if formatado:
        return moeda(num1 + (num1 * (percent / 100.0)), tipoMoeda)
    return num1 + (num1 * (percent / 100.0))
## alternativa para a resolução de formatação
#def aumentar(num1, percent, tipoMoeda='R$', formatado=False):
#    res = moeda(num1 + (num1 * (percent / 100.0)), tipoMoeda)
#    return res if formatado is False else return moeda(res)

def diminuir(num1, percent, tipoMoeda='R$', formatado=False):
    if formatado:
        return moeda(num1 - (num1 * (percent / 100.0)), tipoMoeda)
    return num1 - (num1 * (percent / 100.0))


def dobro(num, tipoMoeda='R$', formatado=False):
    if formatado:
        return moeda(num * 2, tipoMoeda)
    return num * 2


def metade(num, tipoMoeda ='R$', formatado=False):
    if formatado:
        return moeda(num / 2, tipoMoeda)
    return num / 2


def moeda(num, tipoMoeda='R$'):
    return f'{tipoMoeda}{num}'
