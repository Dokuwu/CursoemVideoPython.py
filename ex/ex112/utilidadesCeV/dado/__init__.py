def leiaDinheiro(texto):
    while True:
        m = input(texto)
        if m.isnumeric() is True:
            break
        else:
            print(f'\033[1;31mERRO! "{m}" não é um valor monetario.\033[m')
    return float(m)