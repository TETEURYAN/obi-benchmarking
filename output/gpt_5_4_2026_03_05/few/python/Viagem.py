import sys
import heapq

data = list(map(int, sys.stdin.read().split()))
if not data:
    sys.exit()

V, N, M = data[0], data[1], data[2]
adj = [[] for _ in range(N + 1)]

idx = 3
for _ in range(M):
    a = data[idx]
    b = data[idx + 1]
    t = data[idx + 2]
    p = data[idx + 3]
    idx += 4
    adj[a].append((b, p, t))
    adj[b].append((a, p, t))

X = data[idx]
Y = data[idx + 1]

INF = 10**30
dist = [[INF] * (V + 1) for _ in range(N + 1)]
dist[X][0] = 0

pq = [(0, X, 0)]

while pq:
    time, u, cost = heapq.heappop(pq)
    if time != dist[u][cost]:
        continue
    for v, pc, tt in adj[u]:
        nc = cost + pc
        if nc <= V:
            nt = time + tt
            if nt < dist[v][nc]:
                dist[v][nc] = nt
                heapq.heappush(pq, (nt, v, nc))

ans = min(dist[Y])
print(-1 if ans == INF else ans)