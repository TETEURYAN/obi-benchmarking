import sys
import heapq

input_data = sys.stdin.read().split()
if not input_data:
    exit()

N = int(input_data[0])
M = int(input_data[1])

adj = [[] for _ in range(N + 1)]
idx = 2
for _ in range(M):
    A = int(input_data[idx])
    B = int(input_data[idx + 1])
    C = int(input_data[idx + 2])
    adj[A].append((B, C))
    adj[B].append((A, C))
    idx += 3

dist = [float('inf')] * (N + 1)
dist[1] = 0
pq = [(0, 1)]

while pq:
    d, u = heapq.heappop(pq)
    if d > dist[u]:
        continue
    for v, w in adj[u]:
        if dist[v] > dist[u] + w:
            dist[v] = dist[u] + w
            heapq.heappush(pq, (dist[v], v))

print(dist[N])