import sys

sys.setrecursionlimit(200000)

input_data = sys.stdin.read().split()
if not input_data:
    exit()

N = int(input_data[0])
I = int(input_data[1]) - 1
J = int(input_data[2]) - 1

grid = []
idx = 3
for _ in range(N):
    row = []
    for _ in range(N):
        row.append(int(input_data[idx]))
        idx += 1
    grid.append(row)

visited = [[False] * N for _ in range(N)]
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
count = 0

def dfs(r, c):
    global count
    visited[r][c] = True
    count += 1
    val = grid[r][c]
    
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < N and 0 <= nc < N:
            if not visited[nr][nc] and grid[nr][nc] >= val:
                dfs(nr, nc)

dfs(I, J)
print(count)