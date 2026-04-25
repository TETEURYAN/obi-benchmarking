n = int(input().strip())
a = list(map(int, input().split()))

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
        dist[i] = min(dist[i], last - i)

print(' '.join(str(min(9, d)) for d in dist))