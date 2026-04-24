import sys
import heapq

data = sys.stdin.read().split()
if not data:
    sys.exit()

it = iter(data)
n = int(next(it))
m = int(next(it))

adj = [[] for _ in range(n + 1)]
for _ in range(m):
    u = int(next(it))
    v = int(next(it))
    p = int(next(it))
    adj[u].append((v, p))
    adj[v].append((u, p))

s = int(next(it))

INF = 10**18
dist = [INF] * (n + 1)
dist[s] = 0
pq = [(0, s)]

while pq:
    d, u = heapq.heappop(pq)
    if d != dist[u]:
        continue
    for v, w in adj[u]:
        nd = d + w
        if nd < dist[v]:
            dist[v] = nd
            heapq.heappush(pq, (nd, v))

mn = INF
mx = 0
for i in range(1, n + 1):
    if i == s:
        continue
    if dist[i] < mn:
        mn = dist[i]
    if dist[i] > mx:
        mx = dist[i]

print(mx - mn)