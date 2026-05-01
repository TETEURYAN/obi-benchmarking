import sys
from heapq import heappush, heappop
from collections import defaultdict

data = sys.stdin.read().split()
N = int(data[0])
M = int(data[1])
K = int(data[2])
P = [0] + [int(x) for x in data[3:3 + K]]
edges = []
idx = 3 + K
for _ in range(M):
    v = int(data[idx])
    u = int(data[idx + 1])
    t = int(data[idx + 2])
    edges.append((v, u, t))
    idx += 3
A = int(data[idx])
B = int(data[idx + 1])

adj = [[] for _ in range(N + 1)]
for v, u, t in edges:
    adj[v].append((u, t))
    adj[u].append((v, t))

dist = defaultdict(lambda: defaultdict(lambda: float('inf')))
dist[A][0] = 0
heap = []
heappush(heap, (0, A, 0))
visited = set()

while heap:
    cost, u, s = heappop(heap)
    if (u, s) in visited:
        continue
    visited.add((u, s))
    if cost > dist[u][s]:
        continue
    for v, t in adj[u]:
        if t == s:
            new_cost = cost
            new_s = s
        else:
            new_cost = cost + P[t]
            new_s = t
        if new_cost < dist[v][new_s]:
            dist[v][new_s] = new_cost
            heappush(heap, (new_cost, v, new_s))

min_cost = float('inf')
for s in dist[B]:
    min_cost = min(min_cost, dist[B][s])
if min_cost == float('inf'):
    print(-1)
else:
    print(min_cost)