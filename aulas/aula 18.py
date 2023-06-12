'''teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)'''

'''galera = [['Joao', 19], ['Ana', 33], ['Joaguim', 13], ['Maria', 45]]
print(galera[0][0])
print(galera[2][1])
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade.')'''
galera = list()
dado = list()
for c in range(0,5):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
tmen = tmai = 0
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        tmai += 1
    else:
        print(f'{p[0]} é menor de idade')
        tmen += 1

print(f'Temos {tmai} maiores e {tmen} menores de idade.')