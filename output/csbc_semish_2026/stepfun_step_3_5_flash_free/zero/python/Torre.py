import sys

data = sys.stdin.read().split()
n = int(data[0])
idx = 1
soma_linhas = [0] * n
soma_colunas = [0] * n
matriz = []
for i in range(n):
    linha = list(map(int, data[idx:idx+n]))
    idx += n
    matriz.append(linha)
    for j, val in enumerate(linha):
        soma_linhas[i] += val
        soma_colunas[j] += val
max_peso = 0
for i in range(n):
    for j in range(n):
        peso = soma_linhas[i] + soma_colunas[j] - 2 * matriz[i][j]
        if peso > max_peso:
            max_peso = peso
print(max_peso)