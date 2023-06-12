from datetime import date
pessoa = {}
pessoa['nome'] = str(input('Nome: '))
datcalc = int(input('Ano de nascimento: '))
pessoa['idade'] = date.today().year - datcalc
pessoa['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
if pessoa['ctps'] > 0:
    pessoa['contratação'] = int(input('Ano de contratação: '))
    pessoa['salario'] = float(input('Salario: R$'))
    pessoa['aposentadoria'] = pessoa['idade'] + ((pessoa['contratação'] + 35) - date.today().year )
print('-='*15)
for k,v in pessoa.items():
    print(f' - {k} tem o valor {v}')