cidade = str(input('Digite o nome da sua cidade')).strip()
c = cidade.capitalize()
print(c)
print('Tem Santo no seu nome ?')
print(c[:5] == 'Santo')