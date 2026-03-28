import sys

data = list(map(int, sys.stdin.read().split()))
if not data:
    sys.exit()

n = data[0]
i0 = data[1] - 1
j0 = data[2] - 1

grid = []
idx = 3
for _ in range(n):
    grid.append(data[idx:idx + n])
    idx += n

visited = [[False] * n for _ in range(n)]

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # norte, leste, sul, oeste

stack = [(i0, j0, 0)]  # (i, j, next_dir_to_process)

while stack:
    i, j, d = stack[-1]

    if d == 0 and not visited[i][j]:
        visited[i][j] = True

    if d == 4:
        stack.pop()
        continue

    stack[-1] = (i, j, d + 1)
    ni = i + dirs[(d + 1) % 4][0]
    nj = j + dirs[(d + 1) % 4][1]

    if 0 <= ni < n and 0 <= nj < n:
        if not visited[ni][nj] and grid[ni][nj] >= grid[i][j]:
            stack.append((ni, nj, 0))

ans = 0
for r in range(n):
    for c in range(n):
        if visited[r][c]:
            ans += 1

print(ans)