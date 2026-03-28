import sys

input_data = sys.stdin.read().split()
idx = 0
L = int(input_data[idx]); idx += 1
C = int(input_data[idx]); idx += 1
A = int(input_data[idx]); idx += 1
B = int(input_data[idx]); idx += 1
grid = []
for i in range(L):
    row = []
    for j in range(C):
        row.append(int(input_data[idx]))
        idx += 1
    grid.append(row)

start_r = A - 1
start_c = B - 1
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def get_neighbors(r, c):
    neigh = []
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if 0 <= nr < L and 0 <= nc < C and grid[nr][nc] == 1:
            neigh.append((nr, nc))
    return neigh

current = (start_r, start_c)
prev = None
while True:
    neigh = get_neighbors(current[0], current[1])
    if prev is not None and prev in neigh:
        neigh.remove(prev)
    if not neigh:
        break
    next_pos = neigh[0]
    prev = current
    current = next_pos

print(current[0] + 1, current[1] + 1)