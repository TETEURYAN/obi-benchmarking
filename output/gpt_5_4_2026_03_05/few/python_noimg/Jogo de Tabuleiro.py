import sys

data = list(map(int, sys.stdin.read().split()))
if not data:
    sys.exit()

n = data[0]
board = [[0] * n for _ in range(n)]

idx = 1
for i in range(n):
    for j in range(n):
        board[i][j] = data[idx]
        idx += 1

for i in range(1, n):
    for j in range(1, n):
        s = board[i][j - 1] + board[i - 1][j - 1] + board[i - 1][j]
        board[i][j] = 0 if s >= 2 else 1

print(board[n - 1][n - 1])