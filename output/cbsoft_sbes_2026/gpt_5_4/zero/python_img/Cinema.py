def preco(idade):
    if idade <= 17:
        return 15
    if idade <= 59:
        return 30
    return 20

a = int(input())
b = int(input())

print(preco(a) + preco(b))