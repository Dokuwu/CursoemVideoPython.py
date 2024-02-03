import moeda

boolian = True
while boolian:
    saldo = float(input("Digite seu saldo: R$"))
    if saldo >= 0:
        boolian = False

print(f"Seu saldo com 10% adicionado é {moeda.aumentar(saldo, 10)}")

print(f"Seu saldo com 10% adicionado é {moeda.aumentar(saldo, 10, True)}")

print(f"Seu saldo com 10% retirado é {moeda.diminuir(saldo, 10)}")

print(f"Seu saldo com 10% retirado é {moeda.diminuir(saldo, 10, True)}")

print(f"Seu saldo com dobro é {moeda.dobro(saldo)}")

print(f"Seu saldo com dobro é {moeda.dobro(saldo, True)}")

print(f"Seu saldo com metade é {moeda.metade(saldo)}")

print(f"Seu saldo com metade é {moeda.metade(saldo, True)}")
