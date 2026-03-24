import sys
import heapq

data = sys.stdin.read().split()
if not data:
    sys.exit()

it = iter(data)
N = int(next(it))
M = int(next(it))

size = N + 2
adj = [[] for _ in range(size)]

for _ in range(M):
    s = int(next(it))
    t = int(next(it))
    b = int(next(it))
    adj[s].append((t, b))
    adj[t].append((s, b))

INF = 10**18
dist = [INF] * size
dist[0] = 0
pq = [(0, 0)]

while pq:
    d, u = heapq.heappop(pq)
    if d != dist[u]:
        continue
    if u == N + 1:
        break
    for v, w in adj[u]:
        nd = d + w
        if nd < dist[v]:
            dist[v] = nd
            heapq.heappush(pq, (nd, v))

print(dist[N + 1])