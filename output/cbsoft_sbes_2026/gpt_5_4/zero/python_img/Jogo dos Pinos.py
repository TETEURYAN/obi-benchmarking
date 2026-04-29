board = [input().rstrip('\n') for _ in range(7)]

ans = 0
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for i in range(7):
    for j in range(7):
        if board[i][j] != 'o':
            continue
        for di, dj in dirs:
            ni, nj = i + di, j + dj
            ti, tj = i + 2 * di, j + 2 * dj
            if 0 <= ni < 7 and 0 <= nj < 7 and 0 <= ti < 7 and 0 <= tj < 7:
                if board[ni][nj] == 'o' and board[ti][tj] == '.':
                    ans += 1

print(ans)