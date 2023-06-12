a=float(input('Tamanho em metros '))
print('{}km\n{}hm\n{:.3f}dam\n{}m\n{}dm\n{}cm\n{}mm'.format((a*0.001),(a*0.01),(a*0.1),a,(a*10),(a*100),(a*1000)))
# pro algum motivo o dam dá um numero tipo 0,300000000004