'''pessoas = {'nome':'Gustavo','sexo': 'M','idade': 22}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]}')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
for k in pessoas.keys():
    print(k)
for v in pessoas.values():
    print(v)
for k, v in pessoas.items():
    print(k)
del pessoas['sexo']
pessoas['nome'] = 'Leandro'
pessoas['peso'] = 99.5
for k, v in pessoas.items():
    print(k)'''
'''brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
print(brasil[0])
print(brasil[1]['uf'])
print(brasil[1]['sigla'])
'''
estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}')
for e in brasil:
    for v in e.values():
        print(f'\n{v}', end='')
