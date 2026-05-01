
import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
grid = []
index = 1
pos_r = -1
pos_c = -1
for i in range(N):
    row = []
    for j in range(N):
        val = int(data[index])
        row.append(val)
        if val == 0:
            pos_r = i
            pos_c = j
        index += 1
    grid.append(row)

# Calcular soma mágica
magic_sum = 0
if pos_r != 0:
    for j in range(N):
        magic_sum += grid[0][j]
else:
    for j in range(N):
        magic_sum += grid[1][j]

# Somas das linhas
row_sums = [sum(grid[i]) for i in range(N)]
col_sums = [sum(grid[i][j] for i in range(N)) for j in range(N)]

# Encontrar a soma que falta
missing = 0
if row_sums[pos_r] == 0:
    missing = magic_sum
else:
    for s in row_sums:
        if s != 0 and s != magic_sum:
            missing = s
            break
    if missing == 0:
        for s in col_sums:
            if s != 0 and s != magic_sum:
                missing = s
                break

value = missing - row_sums[pos_r]

# Verificar se é consistente com coluna
if col_sums[pos_c] + value != magic_sum:
    # Se não for, recalcular usando coluna
    missing_col = 0
    for s in col_sums:
        if s != 0 and s != magic_sum:
            missing_col = s
            break
    if missing_col != 0:
        value = missing_col - col_sums[pos_c]

print(value)
print(pos_r + 1)
print(pos_c + 1)
