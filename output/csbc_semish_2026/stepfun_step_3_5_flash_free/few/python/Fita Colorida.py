import sys

data = sys.stdin.read().split()
if not data:
    exit()

n = int(data[0])
arr = list(map(int, data[1:1+n]))

INF = 10**9
dist = [INF] * n

last_zero = -INF
for i in range(n):
    if arr[i] == 0:
        dist[i] = 0
        last_zero = i
    else:
        if last_zero != -INF:
            dist[i] = min(dist[i], i - last_zero)

last_zero = INF
for i in range(n-1, -1, -1):
    if arr[i] == 0:
        dist[i] = 0
        last_zero = i
    else:
        if last_zero != INF:
            dist[i] = min(dist[i], last_zero - i)

result = [str(min(d, 9)) for d in dist]
print(" ".join(result))