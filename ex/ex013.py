a=float(input('Quanto recebe o funcionario?'))
b=int(input('Quanto tem de aumento (%)?'))
print('O salario que vale {}, com {}% de aumento, será {}.'.format(a,b,(a+(a*b/100))))