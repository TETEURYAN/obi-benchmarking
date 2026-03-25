import sys

data = list(map(int, sys.stdin.read().split()))
if not data:
    sys.exit()

n, x, y, z = data
costs = sorted([x, y, z])

count = 0
for c in costs:
    if n >= c:
        n -= c
        count += 1
    else:
        break

print(count)