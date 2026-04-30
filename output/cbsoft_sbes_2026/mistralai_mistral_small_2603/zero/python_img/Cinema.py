idade1 = int(input())
idade2 = int(input())

def calcular_preco(idade):
    if idade <= 17:
        return 15
    elif idade <= 59:
        return 30
    else:
        return 20

total = calcular_preco(idade1) + calcular_preco(idade2)
print(total)