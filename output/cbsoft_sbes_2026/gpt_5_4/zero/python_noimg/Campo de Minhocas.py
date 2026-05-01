import sys

data = list(map(int, sys.stdin.read().split()))
n, m = data[0], data[1]

row_max = 0
col_sums = [0] * m
idx = 2

for _ in range(n):
    row_sum = 0
    for j in range(m):
        v = data[idx]
        idx += 1
        row_sum += v
        col_sums[j] += v
    if row_sum > row_max:
        row_max = row_sum

print(max(row_max, max(col_sums)))