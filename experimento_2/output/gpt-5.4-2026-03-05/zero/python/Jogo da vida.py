import sys

data = sys.stdin.read().strip().split()
if not data:
    sys.exit()

N = int(data[0])
Q = int(data[1])
grid = [list(map(int, list(data[i + 2]))) for i in range(N)]

for _ in range(Q):
    nxt = [[0] * N for _ in range(N)]
    for i in range(N):
        im1 = i - 1
        ip1 = i + 1
        for j in range(N):
            jm1 = j - 1
            jp1 = j + 1
            s = 0
            if im1 >= 0:
                row = grid[im1]
                if jm1 >= 0:
                    s += row[jm1]
                s += row[j]
                if jp1 < N:
                    s += row[jp1]
            row = grid[i]
            if jm1 >= 0:
                s += row[jm1]
            if jp1 < N:
                s += row[jp1]
            if ip1 < N:
                row = grid[ip1]
                if jm1 >= 0:
                    s += row[jm1]
                s += row[j]
                if jp1 < N:
                    s += row[jp1]
            if grid[i][j]:
                nxt[i][j] = 1 if s == 2 or s == 3 else 0
            else:
                nxt[i][j] = 1 if s == 3 else 0
    grid = nxt

sys.stdout.write("\n".join("".join(map(str, row)) for row in grid))