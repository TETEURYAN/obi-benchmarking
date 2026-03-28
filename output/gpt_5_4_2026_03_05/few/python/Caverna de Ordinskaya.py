import sys

data = list(map(int, sys.stdin.read().split()))
if not data:
    sys.exit()

n, m = data[0], data[1]
a = data[2:2+n]

INF = 10**30

prev_low = a[0]
prev_high = m - a[0]
dp_low = prev_low
dp_high = prev_high

for i in range(1, n):
    x = a[i]
    y = m - x

    new_low = INF
    new_high = INF

    if prev_low <= x:
        v = dp_low + x
        if v < new_low:
            new_low = v
    if prev_high <= x:
        v = dp_high + x
        if v < new_low:
            new_low = v

    if prev_low <= y:
        v = dp_low + y
        if v < new_high:
            new_high = v
    if prev_high <= y:
        v = dp_high + y
        if v < new_high:
            new_high = v

    prev_low, prev_high = x, y
    dp_low, dp_high = new_low, new_high

ans = dp_low if dp_low < dp_high else dp_high
print(-1 if ans >= INF else ans)