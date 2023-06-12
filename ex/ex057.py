s = str(input('F ou M? ')).strip().upper()[0]
'''while c != 'M' and c != 'F':
    c = str(input('Digitou errado tente de novo ')).strip().upper()'''
while s not in 'MF':
    s = str(input('Digitou errado tente de novo ')).strip().upper()
print('Sexo {} definido.'.format(s))
