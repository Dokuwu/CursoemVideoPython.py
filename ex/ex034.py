salario = float(input('Digite o seu salario. '))
if salario <= 1250:
    novo = salario + (salario * 0.15)
else:
    novo = salario + (salario * 0.10)
print('O seu salario agora é de {:.2f}'.format(novo))
print('Parabens!')