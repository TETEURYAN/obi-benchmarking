import sys

data = list(map(int, sys.stdin.read().split()))
if not data:
    sys.exit()

n, m = data[0], data[1]
grid = []
idx = 2
start = (-1, -1)
exit_pos = (-1, -1)

for i in range(n):
    row = data[idx:idx + m]
    idx += m
    grid.append(row)
    for j, v in enumerate(row):
        if v == 2:
            start = (i, j)
        elif v == 3:
            exit_pos = (i, j)

x, y = start
px, py = -1, -1
ans = 1

while (x, y) != exit_pos:
    found = False
    if x > 0:
        nx, ny = x - 1, y
        if (nx != px or ny != py) and grid[nx][ny] != 0:
            px, py = x, y
            x, y = nx, ny
            ans += 1
            found = True
    if not found and x + 1 < n:
        nx, ny = x + 1, y
        if (nx != px or ny != py) and grid[nx][ny] != 0:
            px, py = x, y
            x, y = nx, ny
            ans += 1
            found = True
    if not found and y > 0:
        nx, ny = x, y - 1
        if (nx != px or ny != py) and grid[nx][ny] != 0:
            px, py = x, y
            x, y = nx, ny
            ans += 1
            found = True
    if not found and y + 1 < m:
        nx, ny = x, y + 1
        if (nx != px or ny != py) and grid[nx][ny] != 0:
            px, py = x, y
            x, y = nx, ny
            ans += 1
            found = True

print(ans)