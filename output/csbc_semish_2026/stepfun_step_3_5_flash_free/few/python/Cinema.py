import sys

data = sys.stdin.read().split()
idade1 = int(data[0])
idade2 = int(data[1])

def preco(idade):
    if idade <= 17:
        return 15
    elif idade >= 60:
        return 20
    else:
        return 30

total = preco(idade1) + preco(idade2)
print(total)