import sys

data = list(map(int, sys.stdin.read().split()))
if not data:
    sys.exit()

n = data[0]
a = data[1:1 + n]

best = None

for i in range(n):
    if a[i] != 0 and a[i] != 5:
        continue
    for j in range(n):
        if i == j:
            continue
        if j == 0 and a[i] == 0:
            continue
        b = a[:]
        b[i], b[j] = b[j], b[i]
        if best is None or b > best:
            best = b

if best is None:
    print(-1)
else:
    print(*best)