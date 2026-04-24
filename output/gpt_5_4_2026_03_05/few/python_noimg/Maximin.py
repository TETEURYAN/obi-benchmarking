import sys

data = list(map(int, sys.stdin.read().split()))
if not data:
    sys.exit()

n, L, R = data[0], data[1], data[2]
a = data[3:3+n]
a.sort()

best = -10**30

if L <= a[0] <= R:
    val = 0
    if val > best:
        best = val
elif a[0] > R:
    val = a[0] - R
    if val > best:
        best = val

if L <= a[-1] <= R:
    val = 0
    if val > best:
        best = val
elif a[-1] < L:
    val = L - a[-1]
    if val > best:
        best = val

for i in range(n - 1):
    left = a[i]
    right = a[i + 1]
    lo = max(L, left)
    hi = min(R, right)
    if lo > hi:
        continue
    d = (right - left) // 2
    if d > best:
        best = d

print(best)