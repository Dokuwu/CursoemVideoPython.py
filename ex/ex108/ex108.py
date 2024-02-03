import moeda

boolian = True
while boolian:
    saldo = float(input("Digite seu saldo: R$"))
    if saldo >= 0:
        boolian = False
escolha = int(input("O que deseja fazer:\n1- Adicionar saldo %\n2- Remover saldo %\n"
                    "3- Duplicar saldo\n4- Dividir na metade o saldo\n"))

boolian = True

match escolha:
    case 1:
        while boolian:
            percentagem = int(input("Digite valor: %"))
            if percentagem >= 0:
                boolian = False
        saldo = moeda.aumentar(saldo, percentagem)
        print(f"Seu saldo é {moeda.moeda(saldo)}")
    case 2:
        while boolian:
            percentagem = int(input("Digite valor: %"))
            if percentagem >= 0:
                boolian = False
        saldo = moeda.diminuir(saldo, percentagem)
        print(f"Seu saldo é {moeda.moeda(saldo)}")
    case 3:
        saldo = moeda.dobro(saldo)
        print(f"Seu saldo é {moeda.moeda(saldo)}")
    case 4:
        saldo = moeda.metade(saldo)
        print(f"Seu saldo é {moeda.moeda(saldo)}")