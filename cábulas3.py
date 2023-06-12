'TUPLAS'
Lanche (hamburger , sumo, pizza, pudim)
        0   1   2   3

for c in lanche:
    print(c)
vai ficar :
hamburger
sumo
pizza
pudim

'As tuplas são IMUTÁVEIS' ou seja nao tem como modificar os elementos da tupla

sorted(lanche) vai colocar em ordem alfabetica a tupla
lanche.index() vai mostrar o local na memoria que está dentro do index

print('\nO maior valor sorteado foi {}'.format(max(numeros))) vai mostrar o numero maior na tupla
print('O menor valor sorteado foi {}'.format(min(numeros))) vai mostrar o numero menor na tupla


'LISTA'
lanche = [hamburger , sumo, pizza, pudim]
            0         1     2       3

'ADICIONAR'

lanche[3] = gelado
lanche = [hamburger , sumo, pizza, gelado]
            0         1      2     3

lanche.append('Cookie')
lanche = [hamburger , sumo, pizza, gelado, cookie]
            0         1     2       3       4

lanche.insert(0,'cachorro quente')
lanche = [cachorro, hamburger , sumo, pizza, gelado, cookie]
            0        1          2     3       4       5

'TIRAR'

del lanche[3] ou lanche.pop(3) <- o pop é usado apra retirar o ultima mas tb pode para os outros
ou lanche.remove(nome da coisa)

valores = list(range(4,11))
vai contar de 4 a 10 e coloca numa estrutura chamada valores criando uma lista

valores.sort() <- ordena os valores
valores.sort(reverse=True)
len(valores)

dados = list()
dados = ['Pedro', 25, 'Maria', 19, 'Joao', 32]
          0      1    2        3   4       5
pessoas = list()
pessoas.append(dados[:])
pessoas = ['Pedro' 25, 'Maria' 19, 'Joao' 32]
            0           1           2

pessoas = [['Pedro',25],['Maria',19],['Joao',32]]
            0 lista      1 lista     2 lista
print(pessoas[0][0]) == dentro de pessoas 0 ('Pedro',25) vai pegar o de indice 0 que é 'Pedro'
print(pessoas[1][1]) == 19
print(pessoas[2][0]) == 'Joao'
print(pessoas[1]) == ['Maria',19]

'DICIONARIO'
dados = dict() ou dados = {}
dados = {'nome:''Pedro', 'idade':25}
print(dados['nome']) == Pedro
print(dados['idade']) == 25

dados['sexo'] = 'M'
del dados['idade']

filme = {'titulo':'Star Wars',
         'ano':1977
         'diretor':'George Lucas'
}
print(filme.values()) == mostra os valores star wars 1977 etc
print(filme.keys()) == mostra o titulo ano etc
print(filme.items()) == mostra tudo

for k, v in filme.items():
    print(f'O {k} é {v}.') == 'O titulo é Star Wars'

podes colocar um dicionario dentro de uma lista, tupla e vice versa
locadora = [{'titulo':'Star Wars', 'ano':1977, 'diretor':'George Lucas'}, {...etc...}]
print(locadora[0]['ano']) == 1977
print(locadora[2]['titulo']) vai pegar no indice 2 o valor de titulo
Para dicionarios para copiar temos de usar o .copy()
brasil.append(estado.copy())
