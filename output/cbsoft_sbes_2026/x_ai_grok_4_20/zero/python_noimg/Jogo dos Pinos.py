
import sys

board = [line.strip() for line in sys.stdin.readlines()]

directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def is_valid(x, y):
    return 0 <= x < 7 and 0 <= y < 7 and board[x][y] != '-'

count = 0
for i in range(7):
    for j in range(7):
        if board[i][j] == 'o':
            for di, dj in directions:
                ni, nj = i + di, j + dj
                mi, mj = i + 2 * di, j + 2 * dj
                if (is_valid(ni, nj) and board[ni][nj] == 'o' and
                    is_valid(mi, mj) and board[mi][mj] == '.'):
                    count += 1

print(count)
