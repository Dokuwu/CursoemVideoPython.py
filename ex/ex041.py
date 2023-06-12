from datetime import date
ano = int(input('Em que ano nasceu? '))
h = date.today().year
i = h - ano
print('O atleta tem {} anos'.format(i))
if i <= 9:
    print('Você é um nadador \033[1:34mMIRIM\033[m!')
elif i <= 14:
    print('Você é um nadador \033[1:34mINFANTIL\033[m!')
elif i <= 19:
    print('Você é um nadador \033[1:34mJUNIOR\033[m!')
elif i <=25:
    print('Você é um nadador \033[1:34mSENIOR\033[m!')
else:
    print('Você é um nadador \033[1:34mMASTER\033[m!')

#NAO PRECISA COLCOAR MENOR NOS SEGUINTES POIS O ANTERIOR JA RESTRINGE A PROXIMA COMO DE 9 A 14, SE SO COLOCAR MENOR QUE
#14 ELE VAI VERIFICAR QUE O ANTERIOS É DE 9 A MENOS, ESTE SO VAI DO 9 A 14