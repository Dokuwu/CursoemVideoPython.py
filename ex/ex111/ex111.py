from utilidadesCeV import moeda

boolian = True
while boolian:
    saldo = float(input("Digite seu saldo: R$"))
    if saldo >= 0:
        boolian = False
moeda.resumo(saldo,10,10)