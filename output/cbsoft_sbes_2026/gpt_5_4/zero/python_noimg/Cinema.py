def preco(idade):
    if idade <= 17:
        return 15
    elif idade >= 60:
        return 20
    else:
        return 30

a = int(input().strip())
b = int(input().strip())

print(preco(a) + preco(b))