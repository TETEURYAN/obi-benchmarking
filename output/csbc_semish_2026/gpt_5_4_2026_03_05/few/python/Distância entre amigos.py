import sys

data = list(map(int, sys.stdin.read().split()))
if not data:
    sys.exit()

n = data[0]
a = data[1:1 + n]

best_left = a[0] - 1
ans = -10**30

for i in range(1, n):
    val = best_left + a[i] + i
    if val > ans:
        ans = val
    candidate = a[i] - (i + 1)
    if candidate > best_left:
        best_left = candidate

print(ans)