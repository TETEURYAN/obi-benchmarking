import sys

data = list(map(int, sys.stdin.buffer.read().split()))
n = data[0]
vals = data[1:]

board = [vals[i*n:(i+1)*n] for i in range(n)]

row_sum = [sum(row) for row in board]
col_sum = [0] * n

for i in range(n):
    row = board[i]
    for j in range(n):
        col_sum[j] += row[j]

ans = 0
for i in range(n):
    row = board[i]
    rs = row_sum[i]
    for j in range(n):
        w = rs + col_sum[j] - 2 * row[j]
        if w > ans:
            ans = w

print(ans)