lanche = ('Hambúrger', 'Sumo', 'Pizza', 'Pudim', 'Batata Frita')
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')

#Tuplas são imutávais

for comida in lanche:
    print(f'Eu vou comer {comida}')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
print('Comi para caramba!')

print(sorted(lanche))

a = (2, 5, 3)
b = (5, 8, 1, 2)
c = a + b # vai juntar a tupla a com a tupla b
print(c)
print(c.index(2)) #mostra a posição do numero começando do 0
print(c.index(2, 4)) #mostra a posição do numero a partir da posição 4

pessoa = ('Gustavo', 39, 'M', 99.88)
del(pessoa)
print(pessoa)