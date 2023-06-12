cont = s = 0
while True:
    n = float(input('Digite um numero [Digite 999 para parar]. '))
    if n == 999:
        break
    cont += 1
    s += n
print(f'Voce digitou {cont} numeros, e a sua soma é {s:.2f}.')
