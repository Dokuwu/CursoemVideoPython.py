import random
#numero = str(random.randint(0,9999))
#print(numero)
#print("Unidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}".format(numero[3],numero[2],numero[1],numero[0]))

# OUUUUUUUUUUUUUUUUUU

numero = int(input('Digite o seu numero de 0 a 9999 '))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
print("Unidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}".format(u,d,c,m))