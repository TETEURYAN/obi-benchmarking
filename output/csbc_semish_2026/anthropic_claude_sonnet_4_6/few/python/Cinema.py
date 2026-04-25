import sys

def preco(idade):
    if idade <= 17:
        return 15
    elif idade <= 59:
        return 30
    else:
        return 20

data = sys.stdin.read().split()
a1 = int(data[0])
a2 = int(data[1])
print(preco(a1) + preco(a2))