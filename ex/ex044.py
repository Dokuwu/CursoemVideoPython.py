p = float(input('Qual o preço do produto? '))
print('Qual seu metodo de pagamento?')
print('Temos por:\nDinheiro/Cheque e cartão')
m = str(input('')).strip().lower()
if m == 'dinheiro' or m == 'cheque':
    f = p-p*0.10
    print('O preço com 10% de desconto é {}.'.format(f))
elif m == 'cartão' or m == 'cartao':
    v = str(input('Vai pagar 1 vez, 2 vezes, 3 vezes ou mais? ')).strip().lower()
    if v == '1' or v == '1 vez':
        f = p-p*0.05
        print('O preço com 5% de desconto será {}.'.format(f))
    elif v == '2 vezes' or v == '2':
        f = p
        print('O preço será o original, ou seja {} por vez.'.format(f/2))
    elif v == '3' or v == '3 vezes':
        f = p + p * 0.2
        print('O preço levará 20% de juros,será {} por vez.'.format((f)/3))
    elif v == 'mais':
        v2 = int(input('Quantas vezes? '))
        f = p + p * 0.2
        print('O preço terá 20% de juros,será {:.2f} por vez.'.format((f)/v2))
print('Sua compra de {:.2f} será no final {:.2f}.'.format(p, f))
