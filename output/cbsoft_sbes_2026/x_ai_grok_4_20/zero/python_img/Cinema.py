
idade1 = int(input())
idade2 = int(input())

def preco(idade):
    if idade <= 17:
        return 15
    elif idade <= 59:
        return 30
    else:
        return 20

total = preco(idade1) + preco(idade2)
print(total)
