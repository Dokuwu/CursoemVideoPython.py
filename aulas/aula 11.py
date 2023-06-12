'''\033[0;30;41m
\033[4;33;44m
\033[1;35;43m
\033[30;42m --------> nao colocar o 0 so escolhe o estilo do terminal
\033[m --> o padrao do terminal
\033[7;30m'''

#print('\033[0;33;44mOlá, Mundo!\033[m')

a = 3
b = 5
print('Os Valores são \033[32m{}\033[m e \033[31m{}\033[m!!!'.format(a,b))

nome = 'Guanabara'
print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format('\033[4;34m',nome,'\033[m'))

nome = 'Guanabara'
cores = {'limpa' :'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7:30m'}
print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format(cores['amarelo'],nome,cores['limpa']))