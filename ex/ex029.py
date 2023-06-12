velocidade = int(input('Qual é a velocidade de carro? '))
if velocidade <= 80:
    print('Está dentro da lei!')
else:
    multa = (velocidade - 80) * 7
    print('O senhor excedeu o limite de velocidade!')
    print('A sua multa será de {}.'.format(multa))
print('Tenha um bom dia!')