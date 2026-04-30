
idade1 = int(input())
idade2 = int(input())

def preco(idade):
    if idade <= 5:
        return 0
    elif idade <= 12:
        return 10
    elif idade <= 17:
        return 15
    elif idade <= 59:
        return 25
    else:
        return 20

total = preco(idade1) + preco(idade2)
print(total)
