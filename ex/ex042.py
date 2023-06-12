l1 = float(input('O comprimento do primeiro lado: '))
l2 = float(input('O comprimento do segundo lado: '))
l3 = float(input('O comprimento do terceiro lado: '))
if l1 + l2 > l3 and l3 + l2 > l1 and l1 + l3 > l2:
    print('Pode se formar um triangulo')
    if l1 == l2 == l3:
        print('E este é \033[1:34mequilátero\033[m')
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print('E este é \033[1:34misosteles\033[m')
    else:#l1 != l2 or l1 != l3 or l2 !=l3 ou tentao l1 != l2 != l3 !=l1
        print('E este é \033[1:34mescaleno\033[m')
else:
    print('\033[1:31mNão pode ser um triangulo!!!\033[m')