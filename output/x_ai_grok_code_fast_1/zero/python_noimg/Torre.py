
import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
grid = []
index = 1
for i in range(N):
    row = [int(x) for x in data[index:index + N]]
    grid.append(row)
    index += N

soma_linha = [sum(row) for row in grid]
soma_coluna = [0] * N
for j in range(N):
    for i in range(N):
        soma_coluna[j] += grid[i][j]

max_peso = 0
for i in range(N):
    max_for_i = max(soma_coluna[j] - 2 * grid[i][j] for j in range(N))
    peso_i = soma_linha[i] + max_for_i
    if peso_i > max_peso:
        max_peso = peso_i

print(max_peso)
