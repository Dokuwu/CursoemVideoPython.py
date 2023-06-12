f = str(input('Digite uma frase: ')).strip().upper()
lista = f.split()
junto = ''.join(lista)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print('A frase {} no inverso é {}.'.format(junto, inverso))
if inverso == junto:
    print('Temos um palindromo!')
else:
    print('A drase não é um palindromo!')

'''f = str(input('Digite uma frase: ')).strip().upper()
lista = f.split()
junto = ''.join(lista)
inverso = junto[::-1]
print('A frase {} no inverso é {}.'.format(junto, inverso))
if inverso == junto:
    print('Temos um palindromo!')
else:
    print('A drase não é um palindromo!')
'''