import sys

data = sys.stdin.read().split()
if not data:
    sys.exit()

n = int(data[0])
m = int(data[1])
grid = [list(data[i + 2]) for i in range(n)]

for i in range(n):
    for j in range(m):
        if grid[i][j] != '.':
            continue
        wet = False
        if i > 0 and grid[i - 1][j] == 'o':
            wet = True
        elif j > 0 and grid[i][j - 1] == 'o' and i + 1 < n and grid[i + 1][j - 1] == '#':
            wet = True
        elif j + 1 < m and grid[i][j + 1] == 'o' and i + 1 < n and grid[i + 1][j + 1] == '#':
            wet = True
        if wet:
            grid[i][j] = 'o'

sys.stdout.write('\n'.join(''.join(row) for row in grid))