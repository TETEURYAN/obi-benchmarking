import sys
import heapq

input_data = sys.stdin.read().split()
idx = 0
N = int(input_data[idx])
idx += 1
M = int(input_data[idx])
idx += 1

adj = [[] for _ in range(N + 1)]
for _ in range(M):
    U = int(input_data[idx])
    idx += 1
    V = int(input_data[idx])
    idx += 1
    P = int(input_data[idx])
    idx += 1
    adj[U].append((V, P))
    adj[V].append((U, P))

S = int(input_data[idx])

INF = float('inf')
dist = [INF] * (N + 1)
dist[S] = 0
pq = [(0, S)]

while pq:
    d, u = heapq.heappop(pq)
    if d > dist[u]:
        continue
    for v, w in adj[u]:
        if dist[v] > dist[u] + w:
            dist[v] = dist[u] + w
            heapq.heappush(pq, (dist[v], v))

min_dist = INF
max_dist = 0
for i in range(1, N + 1):
    if dist[i] != INF:
        max_dist = max(max_dist, dist[i])
        if i != S:
            min_dist = min(min_dist, dist[i])

print(max_dist - min_dist)