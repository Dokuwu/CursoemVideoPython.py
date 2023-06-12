pessoa = dict()
lista = list()
itotal = 0
#nome sexo idade
while True:
    pessoa['nome'] = str(input('Nome: ')).capitalize()
    while True:
        pessoa['sexo'] = str(input('Sexo: [F/M] ')).strip().upper()[0]
        if pessoa['sexo'] not in 'FM':
            print('ERRO! Digite apenas F ou M')
        else:
            break
    pessoa['idade'] = int(input('Idade: '))
    itotal += pessoa['idade']
    lista.append(pessoa.copy())
    while True:
        r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if r not in 'SN':
            print('ERRO! Digte apenas S ou N')
        else:
            break
    if r in 'N':
        break
print('=-'*30)
print(f'A) Ao todo temos {len(lista)} registrados')
print(f'B) A média de idade é {itotal / len(lista)}')
print('C) As mulheres cadastradas foram: ',end='')
for c in lista:
    if c['sexo'] == 'F':
        print(c['nome'],end=' ')
print('\nD) A lista de pessoas acima da média: ')
for c in lista:
    if c['idade'] > (itotal / len(lista)):
        print(f' nome = {c["nome"]}; sexo = {c["sexo"]}; idade = {c["idade"]}')
        '''
        print('   ', end='')
        for k,v in c.items():
            print(f'{k} = {v}; ', end='')
        print()
        '''
print('<< ENCERRADO >>')
