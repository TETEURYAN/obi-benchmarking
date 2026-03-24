import sys
import heapq

data = sys.stdin.read().split()
if not data:
    exit()

n = int(data[0])
m = int(data[1])

adj = [[] for _ in range(n + 1)]
idx = 2
for _ in range(m):
    a = int(data[idx])
    b = int(data[idx + 1])
    c = int(data[idx + 2])
    adj[a].append((b, c))
    adj[b].append((a, c))
    idx += 3

INF = 10**18
dist = [INF] * (n + 1)
dist[1] = 0
pq = [(0, 1)]

while pq:
    d, u = heapq.heappop(pq)
    if d != dist[u]:
        continue
    if u == n:
        break
    for v, w in adj[u]:
        nd = d + w
        if nd < dist[v]:
            dist[v] = nd
            heapq.heappush(pq, (nd, v))

print(dist[n])