import sys

def is_letter(c):
    return 'A' <= c <= 'Z'

def is_digit(c):
    return '0' <= c <= '9'

def main():
    data = sys.stdin.read().strip()
    if not data:
        return
    placa = data
    n = len(placa)

    # Padrão Brasileiro: 8 caracteres, formato LLL-DDDD
    if n == 8:
        if (is_letter(placa[0]) and is_letter(placa[1]) and is_letter(placa[2]) and
            placa[3] == '-' and
            is_digit(placa[4]) and is_digit(placa[5]) and is_digit(placa[6]) and is_digit(placa[7])):
            print(1)
            return

    # Padrão Mercosul: 7 caracteres, formato LLLDLDD
    if n == 7:
        if (is_letter(placa[0]) and is_letter(placa[1]) and is_letter(placa[2]) and
            is_digit(placa[3]) and
            is_letter(placa[4]) and
            is_digit(placa[5]) and is_digit(placa[6])):
            print(2)
            return

    # Caso contrário, falsificada
    print(0)

if __name__ == "__main__":
    main()