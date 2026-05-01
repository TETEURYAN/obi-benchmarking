
import sys
from heapq import heappush, heappop

input = sys.stdin.read
data = input().split()

N = int(data[0])
M = int(data[1])

graph = [[] for _ in range(N + 1)]

index = 2
for _ in range(M):
    A = int(data[index])
    B = int(data[index + 1])
    C = int(data[index + 2])
    graph[A].append((B, C))
    graph[B].append((A, C))
    index += 3

INF = 10**9
dist = [INF] * (N + 1)
dist[1] = 0

pq = [(0, 1)]

while pq:
    cost, u = heappop(pq)
    if cost > dist[u]:
        continue
    for v, w in graph[u]:
        if dist[u] + w < dist[v]:
            dist[v] = dist[u] + w
            heappush(pq, (dist[v], v))

print(dist[N])
