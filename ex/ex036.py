casa = float(input('Quanto vale a casa? '))
salario = float(input('Qual o seu salário? '))
anos = int(input('Quantos anos vai pagar? '))
meses = anos*12
valor = casa / meses
print('Para pagar uma casa de {:.2f} em {} anos a prestação será {:.2f}.'.format(casa,anos,valor))
if valor <= salario*0.30:
    print('Podemos fazer o emprestimo.')
else:
    print('Não poderemos fazer o emprestimo.')