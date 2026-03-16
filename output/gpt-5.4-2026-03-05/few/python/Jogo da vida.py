import sys

data = sys.stdin.read().split()
if not data:
    sys.exit()

n = int(data[0])
q = int(data[1])
grid = [list(map(int, data[i + 2].strip())) for i in range(n)]

dirs = [(-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)]

for _ in range(q):
    nxt = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            alive = 0
            for di, dj in dirs:
                ni = i + di
                nj = j + dj
                if 0 <= ni < n and 0 <= nj < n:
                    alive += grid[ni][nj]
            if grid[i][j] == 1:
                if alive == 2 or alive == 3:
                    nxt[i][j] = 1
            else:
                if alive == 3:
                    nxt[i][j] = 1
    grid = nxt

out = [''.join(map(str, row)) for row in grid]
sys.stdout.write('\n'.join(out))