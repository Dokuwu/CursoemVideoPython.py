ficha = []
loop = total = 0
while True:
    nome = str(input('Nome: '))
    not1 = float(input('Nota 1: '))
    not2 = float(input('Nota 2: '))
    ficha.append([nome, [not1 , not2]])
    total += 1
    r = str(input('Quer continuar? [S/N] ')).strip().lower()[0]
    if r == 'n':
        break
print('-='*10)
print(f'{"No.":<4}{"NOME":<10}{"MEDIA"}')
print('-'*20)
for i,a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{((a[1][0] + a[1][1])/2):>8.2f}')
print('-'*40)
while True:
    loop = int(input('Qual aluno quer ver as notas ? (Digite 999 para parar) '))
    if loop == 999:
        break
    if loop <= len(ficha) -1:
        print('Notas do {}: {}'.format(ficha[loop][0], ficha[loop][1]))
    print('-'*40)
print('<<< VOLTE SEMPRE >>>')