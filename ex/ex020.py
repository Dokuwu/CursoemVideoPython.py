from random import sample,shuffle
a = str(input('Primeiro aluno: '))
b = str(input('Segundo aluno: '))
c = str(input('Terceiro aluno: '))
d = str(input('Quarto aluno: '))
e = [a,b,c,d]
print('A ordem de apresentação será\n{}'.format(sample(e,4)))

# OUUUUUUUUUUU

a = str(input('Primeiro aluno: '))
b = str(input('Segundo aluno: '))
c = str(input('Terceiro aluno: '))
d = str(input('Quarto aluno: '))
e = [a,b,c,d]
shuffle(e)
print('A ordem de apresentação será\n{}'.format(e))
