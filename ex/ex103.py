def ficha(j='<desconhecido>', g=0):
    print(f'O jogador {j} fez {g} golo(s) no campeonato.')


nome = str(input('Nome do jogador: '))
golos = str(input('Numero de golos: '))
if nome == '' and golos.isnumeric() is False:
    ficha()
elif nome == '':
    ficha(g=golos)
elif golos.isnumeric() is False:
    ficha(nome)
else:
    ficha(nome, golos)
