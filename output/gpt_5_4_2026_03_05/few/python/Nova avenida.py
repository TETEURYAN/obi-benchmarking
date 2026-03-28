import sys

data = list(map(int, sys.stdin.read().split()))
if not data:
    sys.exit()

n = data[0]
m = data[1]

col_sums = [0] * m
idx = 2
for _ in range(n):
    for j in range(m):
        col_sums[j] += data[idx]
        idx += 1

total = sum(col_sums)
best = total

left = 0
for j in range(m - 1):
    left += col_sums[j]
    cost = left
    other = total - left
    if other < cost:
        cost = other
    if cost < best:
        best = cost

print(best)