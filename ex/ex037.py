n = int(input('Digite o seu numero. '))
print('''Para converter temos as seguintes escolhas:')
[1] para binário '
[2] para octal'
[3] para hexadecimal.''')
e = int(input('Qual você quer? '))
if e == 1:
    print(bin(n[2:]))
elif e == 2:
    print(oct(n[2:]))
elif e == 3:
    print(hex(n)[2:])
print('Obrigado por escolher nossos serviços!')