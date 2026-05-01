
import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
index = 1
grid = []
for i in range(N):
    row = [int(data[index + j]) for j in range(N)]
    grid.append(row)
    index += N

# Calcular soma da primeira linha como referência
magic_sum = sum(grid[0])

# Verificar todas as linhas
for i in range(1, N):
    if sum(grid[i]) != magic_sum:
        print(0)
        sys.exit(0)

# Verificar colunas
for j in range(N):
    col_sum = 0
    for i in range(N):
        col_sum += grid[i][j]
    if col_sum != magic_sum:
        print(0)
        sys.exit(0)

# Verificar diagonal principal
diag1 = 0
for i in range(N):
    diag1 += grid[i][i]
if diag1 != magic_sum:
    print(0)
    sys.exit(0)

# Verificar diagonal secundária
diag2 = 0
for i in range(N):
    diag2 += grid[i][N - 1 - i]
if diag2 != magic_sum:
    print(0)
    sys.exit(0)

# Se chegou aqui, é mágico
print(magic_sum)
