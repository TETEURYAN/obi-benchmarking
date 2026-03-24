import sys

data = list(map(int, sys.stdin.read().split()))
if not data:
    sys.exit()

n, k = data[0], data[1]
a = sorted(data[2:2 + n])

INF = 10**18

prev = [INF] * (k + 1)
prev[0] = 0

for i in range(1, n + 1):
    cur = prev[:]
    if i >= 3:
        cost = (a[i - 2] - a[i - 3]) ** 2
        limit = min(k, i // 3)
        for j in range(1, limit + 1):
            val = prev[j - 1] + cost
            if val < cur[j]:
                cur[j] = val
    prev = cur

print(prev[k])