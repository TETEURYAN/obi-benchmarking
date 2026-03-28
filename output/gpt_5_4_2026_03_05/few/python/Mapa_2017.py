import sys

data = sys.stdin.read().split()
if not data:
    sys.exit()

L = int(data[0])
C = int(data[1])
grid = data[2:2 + L]

start_r = start_c = -1
for i in range(L):
    j = grid[i].find('o')
    if j != -1:
        start_r, start_c = i, j
        break

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

prev_r, prev_c = start_r, start_c
cur_r, cur_c = -1, -1

for dr, dc in dirs:
    nr, nc = start_r + dr, start_c + dc
    if 0 <= nr < L and 0 <= nc < C and grid[nr][nc] == 'H':
        cur_r, cur_c = nr, nc
        break

while True:
    next_r, next_c = -1, -1
    for dr, dc in dirs:
        nr, nc = cur_r + dr, cur_c + dc
        if 0 <= nr < L and 0 <= nc < C and grid[nr][nc] == 'H' and not (nr == prev_r and nc == prev_c):
            next_r, next_c = nr, nc
            break
    if next_r == -1:
        print(cur_r + 1, cur_c + 1)
        break
    prev_r, prev_c = cur_r, cur_c
    cur_r, cur_c = next_r, next_c