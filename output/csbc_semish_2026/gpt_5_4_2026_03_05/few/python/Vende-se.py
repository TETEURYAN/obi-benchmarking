import sys

data = list(map(int, sys.stdin.read().split()))
if not data:
    sys.exit()

n, k = data[0], data[1]
x = data[2:2 + n]
x.sort()

m = n - k
ans = x[m - 1] - x[0]

for i in range(1, n - m + 1):
    d = x[i + m - 1] - x[i]
    if d < ans:
        ans = d

print(ans)