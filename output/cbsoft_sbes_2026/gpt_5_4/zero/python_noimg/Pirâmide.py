n = int(input())

for i in range(n):
    linha = []
    for j in range(n):
        valor = min(i, j, n - 1 - i, n - 1 - j) + 1
        linha.append(str(valor))
    print(" ".join(linha))