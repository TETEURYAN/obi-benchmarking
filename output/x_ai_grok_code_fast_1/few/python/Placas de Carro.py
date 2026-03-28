import sys

placa = sys.stdin.read().strip()

def is_letra(c):
    return 'A' <= c <= 'Z'

def is_digito(c):
    return '0' <= c <= '9'

n = len(placa)

if n == 8:
    if (is_letra(placa[0]) and is_letra(placa[1]) and is_letra(placa[2]) and
        placa[3] == '-' and
        is_digito(placa[4]) and is_digito(placa[5]) and is_digito(placa[6]) and is_digito(placa[7])):
        print(1)
    else:
        print(0)
elif n == 7:
    if (is_letra(placa[0]) and is_letra(placa[1]) and is_letra(placa[2]) and
        is_digito(placa[3]) and
        is_letra(placa[4]) and
        is_digito(placa[5]) and is_digito(placa[6])):
        print(2)
    else:
        print(0)
else:
    print(0)