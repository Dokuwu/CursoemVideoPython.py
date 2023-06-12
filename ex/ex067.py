from time import sleep
while True:
    n = int(input('Digite um numero para fazer a tabuada [Digite um numero negativo para parar] '))
    print('-='*15)
    if n < 0:
        break
    for c in range(1,11):
        print(f'{n} X {c:^2} = {n*c} ')
        sleep(0.3)
    print('-='*15)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')