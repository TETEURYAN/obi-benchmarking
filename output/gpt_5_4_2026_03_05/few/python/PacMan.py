import sys

data = sys.stdin.read().split()
if not data:
    exit()

n = int(data[0])
grid = data[1:1 + n]

cur = 0
best = 0

for i in range(n):
    if i % 2 == 0:
        cols = range(n)
    else:
        cols = range(n - 1, -1, -1)
    row = grid[i]
    for j in cols:
        c = row[j]
        if c == 'o':
            cur += 1
        elif c == 'A':
            cur = 0
        if cur > best:
            best = cur

print(best)