def preco(idade):
    if idade <= 17:
        return 15
    elif idade <= 59:
        return 30
    else:
        return 20

a = int(input())
b = int(input())
print(preco(a) + preco(b))