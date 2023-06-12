nome = str(input('O seu nome inteiro, por favor. ')).strip()
dividido = nome.split()
print('O seu nome em maiúsculo é : ',nome.upper())
print('O seu nome em minusculo é : ',nome.lower())
print('O seu nome tem {} letras'.format(len(nome) - nome.count(' ')))
print('O seu primeiro nome tem {} letras'.format(len(dividido[0])))

#OU
#print('O seu nome em maiúsculo é : ',nome.upper())
#print('O seu nome em minusculo é : ',nome.lower())
#print('O seu nome tem {} letras'.format(len(nome) - nome.count(' ')))
#print('O seu primeiro nome tem {} letras'.format(nome.find(' ')))