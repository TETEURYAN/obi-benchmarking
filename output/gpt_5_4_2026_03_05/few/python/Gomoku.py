import sys

data = list(map(int, sys.stdin.read().split()))
board = [data[i * 15:(i + 1) * 15] for i in range(15)]

dirs = ((0, 1), (1, 0), (1, 1), (1, -1))

for i in range(15):
    for j in range(15):
        v = board[i][j]
        if v == 0:
            continue
        for di, dj in dirs:
            pi, pj = i - di, j - dj
            if 0 <= pi < 15 and 0 <= pj < 15 and board[pi][pj] == v:
                continue
            ok = True
            for k in range(1, 5):
                ni, nj = i + di * k, j + dj * k
                if not (0 <= ni < 15 and 0 <= nj < 15 and board[ni][nj] == v):
                    ok = False
                    break
            if ok:
                print(v)
                sys.exit()

print(0)