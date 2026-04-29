import sys

board = [list(map(int, sys.stdin.readline().split())) for _ in range(15)]

dirs = [(0, 1), (1, 0), (1, 1), (1, -1)]

for i in range(15):
    for j in range(15):
        if board[i][j] == 0:
            continue
        color = board[i][j]
        for di, dj in dirs:
            ok = True
            for k in range(1, 5):
                ni, nj = i + di * k, j + dj * k
                if not (0 <= ni < 15 and 0 <= nj < 15 and board[ni][nj] == color):
                    ok = False
                    break
            if ok:
                print(color)
                sys.exit()

print(0)