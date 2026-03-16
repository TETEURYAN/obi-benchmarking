import sys

data = sys.stdin.read().split()
if not data:
    sys.exit()

n = int(data[0])
q = int(data[1])
grid = [[1 if c == '1' else 0 for c in data[i + 2]] for i in range(n)]

for _ in range(q):
    nxt = [[0] * n for _ in range(n)]
    for i in range(n):
        im1 = i - 1
        ip1 = i + 1
        for j in range(n):
            jm1 = j - 1
            jp1 = j + 1
            s = 0
            if im1 >= 0:
                row = grid[im1]
                if jm1 >= 0:
                    s += row[jm1]
                s += row[j]
                if jp1 < n:
                    s += row[jp1]
            row = grid[i]
            if jm1 >= 0:
                s += row[jm1]
            if jp1 < n:
                s += row[jp1]
            if ip1 < n:
                row = grid[ip1]
                if jm1 >= 0:
                    s += row[jm1]
                s += row[j]
                if jp1 < n:
                    s += row[jp1]

            if grid[i][j]:
                if s == 2 or s == 3:
                    nxt[i][j] = 1
            else:
                if s == 3:
                    nxt[i][j] = 1
    grid = nxt

out = [''.join('1' if x else '0' for x in row) for row in grid]
sys.stdout.write('\n'.join(out))