import sys
from collections import defaultdict

data = sys.stdin.read().split()
L = int(data[0])
C = int(data[1])
grid = []
idx = 2
for i in range(L):
    row = data[idx]
    grid.append(list(row))
    idx += 1

# encontrar 'o'
start_i, start_j = -1, -1
for i in range(L):
    for j in range(C):
        if grid[i][j] == 'o':
            start_i, start_j = i, j

# construir grafo
adj = defaultdict(list)
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
for i in range(L):
    for j in range(C):
        if grid[i][j] in ['o', 'H']:
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < L and 0 <= nj < C and grid[ni][nj] in ['o', 'H']:
                    adj[(i, j)].append((ni, nj))

# seguir o caminho
current = (start_i, start_j)
prev = None
while True:
    neighbors = adj[current]
    if prev is not None:
        neighbors = [n for n in neighbors if n != prev]
    if len(neighbors) == 1:
        if prev is not None:
            break
        else:
            next_pos = neighbors[0]
            prev = current
            current = next_pos
    else:
        next_pos = [n for n in neighbors if n != prev][0]
        prev = current
        current = next_pos

print(current[0] + 1, current[1] + 1)