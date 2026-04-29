import sys

data = list(map(int, sys.stdin.read().split()))
if not data:
    sys.exit()

n, m = data[0], data[1]
idx = 2

col_sums = [0] * m
best = 0

for _ in range(n):
    row_sum = 0
    for j in range(m):
        v = data[idx]
        idx += 1
        row_sum += v
        col_sums[j] += v
    if row_sum > best:
        best = row_sum

for s in col_sums:
    if s > best:
        best = s

print(best)