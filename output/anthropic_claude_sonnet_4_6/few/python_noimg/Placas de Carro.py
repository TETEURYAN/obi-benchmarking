import sys

placa = sys.stdin.read().strip()

def is_brasileiro(p):
    if len(p) != 8:
        return False
    if not (p[0].isupper() and p[1].isupper() and p[2].isupper()):
        return False
    if p[3] != '-':
        return False
    if not (p[4].isdigit() and p[5].isdigit() and p[6].isdigit() and p[7].isdigit()):
        return False
    return True

def is_mercosul(p):
    if len(p) != 7:
        return False
    if not (p[0].isupper() and p[1].isupper() and p[2].isupper()):
        return False
    if not p[3].isdigit():
        return False
    if not p[4].isupper():
        return False
    if not (p[5].isdigit() and p[6].isdigit()):
        return False
    return True

if is_brasileiro(placa):
    print(1)
elif is_mercosul(placa):
    print(2)
else:
    print(0)