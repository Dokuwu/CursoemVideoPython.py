n = input('Digite algo: ')
print('Tipo primitivo: ')
print(type(n))
print('É numerico ?')
print(n.isnumeric())
print('É decimal ?')
print(n.isdecimal())
print('É alpha ?')
print(n.isalpha())
print('É alphanumerico ?')
print(n.isalnum())
print('Éstá tudo em maiusculas?')
print(n.isupper())
print('Está tudo em minusculas ?')
print(n.islower())
print('Só tem espaços ?')
print(n.isspace())
print('Está capitalizado ?')
print(n.istitle())

# OUUUUU

a = input("Digite algo ")
print("o tipo primitivo desse valor é ", type(a))
print("só tem espaço ? ", a.isspace())
print("é alfabético ? ", a.isalpha())
print("é alfanumerico ? ", a.isalnum())
print("está em maiúsculo ?", a.isupper())
print("está em minúsculo ?", a.islower())
print("está capitalizada ?", a.istitle())
