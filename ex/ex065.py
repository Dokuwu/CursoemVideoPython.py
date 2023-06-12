c = 'S'
n = maior = menor = s = t = 0
while c == 'S':
    n = int(input('Digite numero inteiro: '))
    s += n
    t += 1
    if t == 1:
        maior = menor = n
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    c = str(input('Deseja continuar [S/N]?')).strip().upper()[0]
print('Voce digitou {} numeros.'.format(t))
print('O maior foi {}, o menor {} e a média de todos os valores é {:.2f}.'.format(maior, menor, s/t))
