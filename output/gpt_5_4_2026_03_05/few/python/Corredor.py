import sys

data = list(map(int, sys.stdin.read().split()))
if not data:
    sys.exit()

n = data[0]
a = data[1:1+n]

best = a[0]
current = a[0]

for x in a[1:]:
    current = max(x, current + x)
    if current > best:
        best = current

print(best)