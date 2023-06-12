t = 0
mu = 0
ivelho = 0
nome = ''
for c in range(1, 5):
    print('------{}º PESSOA------'.format(c))
    n = str(input('Digite o nome: ')).strip().title()
    i = int(input('Digite a idade: '))
    s = str(input('Sexo [F/M]? ')).strip().lower()
    t += i
    if c == 1 and s == 'm':
        ivelho = i
        nome = n
    if s == 'm' and i > ivelho:
        ivelho = i
        nome = n
    if s == 'f' and i < 21:
        mu = mu + 1
print('A media da idade das pessoas foi {}.'.format(t/4))
if ivelho == 0:
    pass
else:
    print('O homem mais velho tem {} anos e chama-se {}.'.format(ivelho, nome))
if mu == 1:
    print('Tem {} mulher debaixo dos 20.'.format(mu))
else:
    print('Tem {} mulheres debaixo dos 20.'.format(mu))
