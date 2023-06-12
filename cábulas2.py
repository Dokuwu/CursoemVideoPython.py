
Padrão ANSI ele tem escape sequence, vamos usar para o terminal
\033[(codigo da cor)m
\033[0 ou 1 ou 2 ou 3 codigosm
\033[estilo,texto,backgroundm
\033[0;33;44m
estilo temos 0,1,4 e 7 (0 é o original)(1 é em negrito)(4 é sublinhado)(7 inverte as cores)

texto temos 30 a 37 (30 branco)(.1 vermelho)(.2 verde)(.3 amarelo)(.4 azul)(.5 roxo)(.6 ciano)(.7 cinzento) para ter
mais core tem de usar outras bibliotecas ou funcionalidades

EXISTE UMA BIBLIOTECA CHAMADA COLORIZE QUE TEM MAIS OPÇOES

background temos 40 a 47 (40 branco)(.1 vermelho)(.2 verde)(.3 amarelo)(.4 azul)(.5 roxo)(.6 ciano)(.7 cinzento)

if       else
true     false
if       elif     else
se     senao se   senao
if elif elif elif elif else
pode usar quantos elif quiser

condição aninhada tem uma coisa dentro da outra

'''Laços de''' '''REPETIÇÕES ou ITERAÇÃO'''

laço c no intervalo(1,10)  (c é a variavel de controle)
    passo
pega

for c in range(1,10):
    passo
pega

lao c no intervalo(0,3)
    passo
    pula
passo
pega

for c in range(0,3):
    passo
    pula
passo
pega

lao c no intervalo(0,3)
    se tiver moeda
        pega
    passo
    pula
passo
pega

for c in range(0,3):
    if tiver moeda:
        pega
    passo
    pula
passo
pega

for estrutura de repitição com variavel

while estrutura de repitição logica

while = enquanto

while c != maça:
    passo
pega

while != maça:
    if bloco:
        passo
    if vazio:
        pula
    if moeda:
        pega
pega

while True:
    if bloco:
        passo
    if vazio:
        pula
    if moeda:
        pega
    if trofeu:
        pula
        break # interrompa
pega

n = float(input('numero '))
print(f'O seu valor é {n:.2f}.') NOVA MANEIRA DE FAZER STRING: FSTRINGS


while True:
    c = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if c in 'SN':
        break

 ouuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu

c = ' '
while c not in 'SN':
    c = str(input('bla bla bla')).strip().upper()[0]
