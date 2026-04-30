
board = [input().strip() for _ in range(7)]

directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

count = 0
for i in range(7):
    for j in range(7):
        if board[i][j] != 'o':
            continue
        for di, dj in directions:
            ni, nj = i + di, j + dj
            mi, mj = i + 2 * di, j + 2 * dj
            if (0 <= ni < 7 and 0 <= nj < 7 and
                0 <= mi < 7 and 0 <= mj < 7 and
                board[ni][nj] == 'o' and
                board[mi][mj] == '.'):
                count += 1

print(count)
