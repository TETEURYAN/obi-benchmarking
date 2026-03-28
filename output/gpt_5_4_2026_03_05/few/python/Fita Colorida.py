import sys

data = list(map(int, sys.stdin.read().split()))
if not data:
    exit()

n = data[0]
a = data[1:1 + n]

INF = 10**9
dist = [INF] * n

last = -INF
for i in range(n):
    if a[i] == 0:
        last = i
        dist[i] = 0
    else:
        dist[i] = i - last

last = INF
for i in range(n - 1, -1, -1):
    if a[i] == 0:
        last = i
    else:
        d = last - i
        if d < dist[i]:
            dist[i] = d

for i in range(n):
    if dist[i] > 9:
        dist[i] = 9

print(*dist)