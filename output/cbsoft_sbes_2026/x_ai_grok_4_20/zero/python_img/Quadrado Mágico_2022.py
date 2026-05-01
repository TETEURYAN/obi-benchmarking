
import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
grid = []
index = 1
for i in range(N):
    row = []
    for j in range(N):
        row.append(int(data[index]))
        index += 1
    grid.append(row)

# Encontrar posição do zero
rx, cy = -1, -1
for i in range(N):
    for j in range(N):
        if grid[i][j] == 0:
            rx, cy = i, j
            break
    if rx != -1:
        break

# Calcular soma mágica
magic = 0
if rx != 0:
    magic = sum(grid[0])
else:
    magic = sum(grid[1])

# Soma da linha do zero
row_sum = sum(grid[rx])

# Soma da coluna do zero
col_sum = 0
for i in range(N):
    col_sum += grid[i][cy]

# Verificar diagonais se aplicável
diag1 = 0
diag2 = 0
is_diag1 = (rx == cy)
is_diag2 = (rx + cy == N - 1)

if is_diag1:
    for i in range(N):
        diag1 += grid[i][i]
if is_diag2:
    for i in range(N):
        diag2 += grid[i][N - 1 - i]

# Determinar o valor faltante
if row_sum != magic:
    missing = magic - row_sum
elif col_sum != magic:
    missing = magic - col_sum
elif is_diag1 and diag1 != magic:
    missing = magic - diag1
elif is_diag2 and diag2 != magic:
    missing = magic - diag2
else:
    # Caso em que a linha e coluna estão corretas mas precisamos usar outra linha/coluna
    # Tenta usar outra linha
    for i in range(N):
        if i != rx:
            s = sum(grid[i])
            if s == magic:
                missing = magic - row_sum
                break

print(missing)
print(rx + 1)
print(cy + 1)
