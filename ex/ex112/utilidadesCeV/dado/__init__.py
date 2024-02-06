
def leiaDinheiro(texto):
    while True:
        m = str(input(texto)).replace(",",".").strip()
        if m.isalpha() is False:
            break
        else:
            print(f'\033[1;31mERRO! "{m}" não é um valor monetario.\033[m')
    return float(m)
