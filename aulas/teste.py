
def magia(idade):
    idade += 1
    idade *= 2
    idade -= 2
    return idade
dict = {'idade':int(0), 'Nome':'NULL'}
i = "!"
print(f"Digite a sua idade {i}")
idade = int(input("Digite a sua idade"))

for c in range(1, 2):
    idade = magia(idade)

frase = str(input("Digite uma frase"))

frase.lower().split().reverse()
for k in frase:
    print(k)

dict['Nome'] = str(input("Digite seu nome")).title()
dict['idade'] = idade
print(f"Nome: {dict['Nome']} Idade: {dict['idade']}")

