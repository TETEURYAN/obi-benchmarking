import sys

data = sys.stdin.read().split()

N = int(data[0])

grid = []

idx = 1

for i in range(N):
    row = [int(x) for x in data[idx:idx+N]]
    grid.append(row)
    idx += N

# Verificar se os números são exatamente 1 a N*N sem repetições
all_nums = set()
for row in grid:
    for num in row:
        if num in all_nums or num < 1 or num > N*N:
            print(0)
            sys.exit()
        all_nums.add(num)
if len(all_nums) != N*N:
    print(0)
    sys.exit()

# Calcular soma da primeira linha como referência
target = sum(grid[0])

# Verificar linhas
for row in grid:
    if sum(row) != target:
        print(0)
        sys.exit()

# Verificar colunas
for j in range(N):
    col_sum = 0
    for i in range(N):
        col_sum += grid[i][j]
    if col_sum != target:
        print(0)
        sys.exit()

# Diagonal principal
diag1 = 0
for i in range(N):
    diag1 += grid[i][i]
if diag1 != target:
    print(0)
    sys.exit()

# Diagonal secundária
diag2 = 0
for i in range(N):
    diag2 += grid[i][N-1-i]
if diag2 != target:
    print(0)
    sys.exit()

# Se passou tudo, imprimir target
print(target)