import sys
import heapq

input_data = sys.stdin.read().split()
N = int(input_data[0])
M = int(input_data[1])
graph = [[] for _ in range(N + 2)]
idx = 2
for _ in range(M):
    S = int(input_data[idx])
    T = int(input_data[idx + 1])
    B = int(input_data[idx + 2])
    graph[S].append((T, B))
    graph[T].append((S, B))
    idx += 3

dist = [float('inf')] * (N + 2)
dist[0] = 0
pq = [(0, 0)]
while pq:
    d, u = heapq.heappop(pq)
    if d > dist[u]:
        continue
    for v, w in graph[u]:
        if dist[v] > dist[u] + w:
            dist[v] = dist[u] + w
            heapq.heappush(pq, (dist[v], v))
print(dist[N + 1])