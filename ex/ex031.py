distancia = float(input('Qual a distancia da viagem em km? '))
if distancia <= 200:
    p1 = distancia * 0.5
    print('O preço da viagem vai ser {:.2f}$R.'.format(p1))
else:
    p2 = distancia * 0.45
    print('O preço da viagem vai ser {:.2f}$R.'.format(p2))
print('Tenha uma boa viagem!')

# ouuuuuuuuuuuuuuuuuuu

distancia = float(input('Qual a distancia da viagem em km? '))
preço = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('O preço da viagem vai ser {:.2f}$R.'.format(preço))
print('Tenha uma boa viagem!')