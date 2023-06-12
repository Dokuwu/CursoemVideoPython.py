def voto(a):
    from datetime import date
    hoje = date.today().year
    idade = hoje - a
    if idade < 16:
        print(f'Com {idade} anos: NÃO VOTA')
    elif idade >= 18:
        print(f'Com {idade} anos: VOTO OBRIGATORIO')
    elif 16 <= idade < 18 or idade >= 65:
        print(f'Com {idade} anos: VOTO OPCIONAL')


print('-'*30)
ano = int(input('Ano de nascimento: '))
voto(ano)
