print = mostrar na tela
input = receber algo escrito e igual a uma variavel
int = tornar um numero inteiro (7;-4;0)
float = reais ou ponto flutuante (4.5;0.076;-15.223;7.0)
bool = logicos (True;False)
str = caracteres ou streams ('Olá';'7.5';'') AS ASPAS
print('A soma vale {}'.format(s)) otura forma de fazer print
print(type(a)) mostrar o tipo ^ os de cima

n = input('Digite algo: ')
print(n.isnumeric)
#o isnumeric verifica se é um numero, se for aparece true

Ordem de precedencia
1-()
2-** potencia
3-* ;/ ;// (divisao total) ;% (resto da divisao) NAO E COMO NA MATEMATICA FAZ QUEM APARECER PRIMEIRO
4- + ; -

O '==' significa IQUAL e o '!=' significa DIFERENTE

print('Prazer em te conhecer {:^20}!'.format(nome))
o {:^20} significa que vai escrever a variavel "nome" em 20 caracteres. E o :^ vai escreve-lo centralizado
O :< vai centralizar a esquerda e o :> à direita
{:=^20} o = vai colocar à volta do nome = por exemplo vai aparecer =====Ana=====
{:.3f}= 3 casas decimais
end='' NO FINAL NAO VAI QUEBRAR A LINHA
\n :quebra de linha

import serve para importar bibliotecas ou modulos
(import math) IMPORTA TUDO para so escolher 1 modulo faz (from math import 'nome')
para usar o modulo coloca math.nomedomodulo por exemplo
'from math import sqrt,ceil' se estiver assim so precisa de colocar o modulo para usa-lo

random math sao bibliotecas importantes

Uma lista fica entre []

STRING é uma frase do tipo 'Curso em Video Python'

'FATIAMENTO DE UMA STRING'

'frase[9]' --->vai identificar so o caractar o micro espaço 9 (o micro espaço é o caractere)
espaço numera de 0 a ultimo caracter pro exempo (Caramelo é bom) seria de 0 a 13 os espaços contam

'frase [9:13]' ---> pega do 9 até o 13 excluindo o 13

'se uma string vai até o 20'
frase[9:21] vai do 9 até o 20

'frase[9:21:2]' do 9 ao 20 pulando 2 em 2 por exemplo (video python) seria 'vdopto'

frase[x:y] o x é antes dos dois pontos é onde começa o y é depois dos dois pontos e é onde acaba

'frase[:5]' ----> começa do 0 e vai até o 4

'frase[15:]' do 15 ao ultimo

'frase[9::3]' começa no 9 entre os dois pontos, começa no 9 e vai até o final e depois do segundo dois
pontos vai pulando 3 em 3

len(frase) mostra o comprimento da frase quantos caracteres

frase.count('o') conta quantos letras dentro das aspas tem a string, aqui contaria quantos 'o' teria

frase.count('o',0,13) do 0 até o 12 vai contar os 'o'

frase.find('deo') quantas vezes encontrou 'deo'

frase.find('Android') quando procura algo que nao existe na string ele mostra -1

'Curso' in frase ele ve se tem o entre aspas se sim ele mostra True

'TRANSFORMAÇÃO DE STRING'

frase.replace('Python','Android') substitui o primeiro ,Python, pelo segundo,Android.

frase.upper() --> o que for minusculo torna-o em maiusculo

frase.lower() --> o que for maiusculo torna-o em minusculo

frase.capitalize() --> joga todos os caracteres para minusculo e só o primeiro caracter fica em maiusculo

frase.title() --> analise quantas palavras tem a string onde tem espaço quebra a palavras
e faz o capitalize em cada palavra, ou seja todas ficam capitalizadas

'(   Aprenda Python  )

frase.strip() ---> Tira todos os espaços inuteis ou seja a frase em cima ficaria (Aprenda Python)

frase.rstrip() --> tira os espaços inuteis na direita

frase.lstrip() --> tira os espaços inuteis na esquerd

'DIVISSÃO DE STRING'

frase.split() onde tem espaço cria uma divisão e forma uma lista por exemplo: (Curso em Vídeo Python) ficaria
(Curso) (em) (Vídeo) (Python)

'JUNÇÃO DE STRING'

'-'.join(frase) junta todos os elementos de frase e vai usar o separador '-' entre eles por exemplo:
(Olá) (Mundo) ficaria (Olá-Mundo)

frase = 'Curso em Vídeo Python'
frase = frase.replace('Python','Android') VAI SALVAR A MODIFICAÇÃO DE COLCOAR FRASE =

dividido = frase.split()
print(dividido[0])

forma a frase em lista e depois mostra o primeiro

print(dividido[2][3])

pega o 2 da lista e mostre a letra 3
