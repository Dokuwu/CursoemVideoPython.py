#if --> se | ficaria if carro.esquerda():
 #   bloco True
#else --> senão
 #   bloco False

tempo = int(input('Quantos anos tem seu carro?'))
if tempo <= 3:
    print('carro novo')
else:
    print('carro velho')
print('--FIM--')

#ouuuuuuuuuuuuuuuuuuuu

tempo = int(input('Quantos anos tem seu carro?'))
print('carro novo'if tempo <= 3 else 'carro velho')
print('--FIM--')

#-----------------------------------------------------------------------------------

nome = str(input('Qual é seu nome? '))
if nome == 'Gustavo':
    print('QUe nome lindo você tem!')
else:
    print('Que nome tão normal!')
print('Bom dia ',nome)

#-------------------------------------

n1 = float(input('Digite a primeira nota'))
n2 = float(input('Digite a segunda nota'))

m = (n1 + n2)/2

print('A sua média foi {:.1f}'.format(m))
if m >= 6.0:
    print('Sua média foi boa! PARABENS!')
else:
    print('Sua média foi ruim! ESTUDE MAIS!')

ouuuuuu
print('PARABENS' if m >=6 else 'MELHORE')
