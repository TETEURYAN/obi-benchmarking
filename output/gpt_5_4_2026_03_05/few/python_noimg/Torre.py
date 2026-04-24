import sys

data = list(map(int, sys.stdin.read().split()))
if not data:
    sys.exit()

n = data[0]
board = [[0] * n for _ in range(n)]
row_sum = [0] * n
col_sum = [0] * n

idx = 1
for i in range(n):
    s = 0
    row = board[i]
    for j in range(n):
        v = data[idx]
        idx += 1
        row[j] = v
        s += v
        col_sum[j] += v
    row_sum[i] = s

ans = 0
for i in range(n):
    rs = row_sum[i]
    row = board[i]
    for j in range(n):
        w = rs + col_sum[j] - row[j]
        if w > ans:
            ans = w

print(ans)