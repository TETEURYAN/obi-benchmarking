import sys

data = list(map(int, sys.stdin.read().split()))
if not data:
    sys.exit()

L, C = data[0], data[1]
A, B = data[2] - 1, data[3] - 1

grid = [[0] * C for _ in range(L)]
idx = 4
for i in range(L):
    row = data[idx:idx + C]
    grid[i] = row
    idx += C

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

prev_r, prev_c = -1, -1
r, c = A, B

while True:
    next_r, next_c = -1, -1
    count = 0
    for dr, dc in dirs:
        nr, nc = r + dr, c + dc
        if 0 <= nr < L and 0 <= nc < C and grid[nr][nc] == 1 and not (nr == prev_r and nc == prev_c):
            next_r, next_c = nr, nc
            count += 1
    if count == 0:
        print(r + 1, c + 1)
        break
    prev_r, prev_c, r, c = r, c, next_r, next_c