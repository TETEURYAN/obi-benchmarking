import sys
from bisect import bisect_right

data = list(map(int, sys.stdin.read().split()))
if not data:
    sys.exit()

n = data[0]
x = data[1:1 + n]
h = data[1 + n:1 + 2 * n]

reach = [0] * n
for i in range(n):
    r = bisect_right(x, x[i] + h[i]) - 1
    reach[i] = r

LOG = n.bit_length()
up = [[0] * n for _ in range(LOG)]
mx = [[0] * n for _ in range(LOG)]

for i in range(n):
    up[0][i] = min(reach[i] + 1, n - 1)
    mx[0][i] = reach[i]

for k in range(1, LOG):
    up_prev = up[k - 1]
    mx_prev = mx[k - 1]
    up_cur = up[k]
    mx_cur = mx[k]
    for i in range(n):
        j = up_prev[i]
        up_cur[i] = up_prev[j]
        a = mx_prev[i]
        b = mx_prev[j]
        mx_cur[i] = a if a >= b else b

ans = [0] * n
for i in range(n - 1, -1, -1):
    cur = i
    best = reach[i]
    for k in range(LOG - 1, -1, -1):
        m = mx[k][cur]
        if m > best:
            best = m
            cur = up[k][cur]
    ans[i] = best - i + 1

print(*ans)