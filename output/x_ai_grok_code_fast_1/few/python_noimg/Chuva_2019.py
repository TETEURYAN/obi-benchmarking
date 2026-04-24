import sys

input_data = sys.stdin.read().split()
idx = 0
N = int(input_data[idx])
idx += 1
M = int(input_data[idx])
idx += 1

grid = []
for i in range(N):
    row = list(input_data[idx])
    idx += 1
    grid.append(row)

o_positions = set()
queue = []
for i in range(N):
    for j in range(M):
        if grid[i][j] == 'o':
            o_positions.add((i, j))
            queue.append((i, j))

while queue:
    i, j = queue.pop(0)
    # propagar para baixo
    if i + 1 < N and grid[i + 1][j] == '.':
        grid[i + 1][j] = 'o'
        if (i + 1, j) not in o_positions:
            o_positions.add((i + 1, j))
            queue.append((i + 1, j))
    # se há prateleira abaixo, escorrer para esquerda e direita
    if i + 1 < N and grid[i + 1][j] == '#':
        if j - 1 >= 0 and grid[i][j - 1] == '.':
            grid[i][j - 1] = 'o'
            if (i, j - 1) not in o_positions:
                o_positions.add((i, j - 1))
                queue.append((i, j - 1))
        if j + 1 < M and grid[i][j + 1] == '.':
            grid[i][j + 1] = 'o'
            if (i, j + 1) not in o_positions:
                o_positions.add((i, j + 1))
                queue.append((i, j + 1))

for row in grid:
    print(''.join(row))