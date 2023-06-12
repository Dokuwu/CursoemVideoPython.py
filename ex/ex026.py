frase = str(input('Digite uma frase ')).lower().strip()
print('A sua frase tem {} (a)\nO primeiro (a) aparece no caractere {}\nO ultimo (a) aparece no caractere {}'
.format(frase.count('a'),frase.find('a')+1,frase.rfind('a')+1))