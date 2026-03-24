import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

L = int(input_data[0])
C = int(input_data[1])
grid = input_data[2:]

start_r = -1
start_c = -1

for i in range(L):
    for j in range(C):
        if grid[i][j] == 'o':
            start_r = i
            start_c = j
            break
    if start_r != -1:
        break

visited = [[False] * C for _ in range(L)]
visited[start_r][start_c] = True

curr_r, curr_c = start_r, start_c
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

while True:
    moved = False
    for dr, dc in directions:
        nr, nc = curr_r + dr, curr_c + dc
        if 0 <= nr < L and 0 <= nc < C:
            if grid[nr][nc] == 'H' and not visited[nr][nc]:
                curr_r, curr_c = nr, nc
                visited[nr][nc] = True
                moved = True
                break
    if not moved:
        break

print(f"{curr_r + 1} {curr_c + 1}")