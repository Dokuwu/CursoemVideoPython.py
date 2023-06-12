peso = float(input('Quanto você pesa em \033[1:34mQUILOGRAMAS\033[m? '))
altura = float(input('Qual a sua altura em \033[1:34mMETROS\033[m? '))
imc = peso / (altura * altura)
print('O seu \033[1:34mIMC\033[m é \033[1:31m{:.2f}\033[m, o que significa...'.format(imc))
if imc < 18.5:
    print('\033[1:31mVOCÊ ESTÁ ABAIXO DO PESO!!!\033[m')
elif 18.5 <= imc < 25:
    print('\033[1:32mParabens!!! Você está no peso ideal.\033[m')
elif 25 <= imc < 30:
    print('\033[1:33mEstá sobrepeso, preciamos emagrecer um pouco!!!\033[m')
elif 30 <= imc < 40:
    print('\033[1:31mObesidade... Estamos num mau caminho, é melhor começar a emagrecer.\033[m')
else:
    print('\033[1:31mOBESIDADE MÓRBIDA!!!! PRECISAMOS DE UMA MUDANÇA IMEDIATA NA SUA DIETA!!!\033[m')