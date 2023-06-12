def notas(*num, sit=False):
    """
    --> Comando para analisar notas e informações dos alunos
    :param num: uma ou mais notas dos alunos (podem ser varias)
    :param sit: (opcional) indica se deve ou não mostrar a situação
    :return: um dicionario com varias informações sobre a situação da turma
    """
    cont = maior = menor = tot = 0
    dic = dict()
    for c in num:
        if cont == 0:
            maior = c
            menor = c
            cont += 1
        if maior < c:
            maior = c
        if menor > c:
            menor = c
        tot += c
    dic['total'] = len(num)
    dic['maior'] = maior
    dic['menor'] = menor
    dic['media'] = tot / len(num)
    if sit is True:
        if tot / len(num) >= 7:
            dic['situação'] = 'BOA'
        elif 4 <= (tot / len(num)) < 7:
            dic['situação'] = 'RAZOAVEL'
        else:
            dic['situação'] = 'RUIM'
    return dic


resp = notas(6, 11, 11, sit=True)
print(resp)
