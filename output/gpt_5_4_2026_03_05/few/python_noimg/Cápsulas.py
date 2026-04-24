import sys

data = list(map(int, sys.stdin.read().split()))
if not data:
    sys.exit()

n, f = data[0], data[1]
c = data[2:2 + n]

lo, hi = 0, 100000000

while lo < hi:
    mid = (lo + hi) // 2
    total = 0
    for x in c:
        total += mid // x
        if total >= f:
            break
    if total >= f:
        hi = mid
    else:
        lo = mid + 1

print(lo)