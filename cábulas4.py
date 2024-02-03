'Função ou Def'
def mostralinha():
    print('-'*50)
#entre o def e programa principal tem de ter duas linhas vazias
#criou uma rotina no qual quando usar o mostralinha() vai mostrar o print('-'*50)
mostralinha()
print('     SISTEMA DE ALUNOS     ')
mostralinha()
print('     CADASTRO DE FUNCIONARIOS   ')
mostralinha()

def mensagem(msg):#pode ser qualquer coisa o msg
    print('-'*40)
    print(msg)
    print('-'*40)


mensagem('     SISTEMA DE ALUNOS     ')
mensagem('     OPPA GANGSTA STYLE    ')
mensagem('Oi')

ISTO CHAMA-SE EMPACOTAMENTO
O * SIGNIFICA DESEMPACOTAR
def contador(*num):
    print(num)


contador(5, 7, 3, 1, 4)
contador(8, 4, 7)

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1

valores = [7, 2, 5, 0, 4]
dobra(valores)
print(valores)

'Interactive help'

no python console digite help() e entao digite a fnção que tens duvida
quit para sair

outro metodo é no proprio ficheiro:
help(print)
print(input.__doc__) vai mostrar o doc da função antes do .__doc__

'Docstrings'

help(input) mostra a docstring do input()

Se for outra pessoa a usar este codigo nao vai entender o que é
def contagem(a, b, c):
    '''
    -> Faz uma contagem e mostra na tela
    :param i: inicio da contagem
    :param f: fim da contagem
    :param p: passo de contagem
    :return: sem retorno
    '''
    print('=-' * 25)
    print(f'Contagem de {c} até {b} de {c} em {c}')
    if a < b:
        for d in range(a, b + 1, c):
            print(d, end=' ')
            sleep(0.25)
    elif a > b:
        for d in range(a, b - 1, -c):
            print(d, end=' ')
            sleep(0.25)

help(contador) so vai aparecer algo se colocar 3 aspas e escrever algo no meio
param = parametros
return = retorno

'Parametros opcionais'

def somar(a, b, c=0):
    s = a + b + c
    print(s)


somar(3,2,5)
somar(8,4)

o =0 vai tornar o c em 0 tornando-o opcional

'Escopo de variaveis'
def teste(n):
    global n
    n = 5
    x = 8
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x}')
n = 2
print(f'No programa princival n vale {n}')
teste(n)
print(f'No programa principal, x vale {x}')

O n resulta no progrma principal e na função teste, sendo uma variavel global

o x so tem no teste e so resulta nela, sendo uma variavel local

o n tem escopo global e o x tem escopo local

Porem se colocar global n para usar o n global, no qual vai ateral o n em tudo


O n no programa principal é escopo global
Porem o n na função teste é escopo local, no qual criou uma variavel 'a' na função com o valor 5

'Retornando valores'
def somar(a=0,b=0,c=0):
    s = a + b + c
    return s

r1 = somar(2,2,3)
r2 = somar(2,2)
r3 = somar(4)

o return s vai returnar o s para o que vier antes como uma variavel ou até um print

'   MODULOS     '

Cria um ficheiro py separado com as funções que quer usar por exemplo uteis.py

No outro ficheiro é so fazer import uteis e usar depois ex: uteis.factorial()

' JUNÇAO DE MODULOS (PACOTES)'

quando um modulo fica muito grande, antigamente separavasse em mais modulos
mas o python permite criar pacote, junção de modulos num so ficheiro
por exemplo um pacote util, pode ter os modulos numeros,strings,datas
depois é o mesmo import util, ou se quiser algo mais especifico, from util import numeros

a criação é feita por pastas
cria a pasta util, e dentro dessa pasta tem mais pastas,cada uma com o nome dos modulos
cada pasta modulo deve ter o ficheiro __init__.py mas ele ja cria por si só

como fazer : botao direito e em new tem como selecionar python package, e entao só fazer o mesmo, dentro do outro package
para criar ainda mais packages ou modulos

para adicionar funções, coloca dentro do ficheiro __init__.py