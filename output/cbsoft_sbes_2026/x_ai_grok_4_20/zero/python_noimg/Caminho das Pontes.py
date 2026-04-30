
import sys
from heapq import heappush, heappop

input = sys.stdin.read
data = input().split()

N = int(data[0])
M = int(data[1])
index = 2

graph = [[] for _ in range(N + 2)]
for _ in range(M):
    S = int(data[index])
    T = int(data[index + 1])
    B = int(data[index + 2])
    graph[S].append((T, B))
    graph[T].append((S, B))
    index += 3

INF = 10**9
dist = [INF] * (N + 2)
dist[0] = 0

pq = [(0, 0)]

while pq:
    cost, u = heappop(pq)
    if cost > dist[u]:
        continue
    for v, w in graph[u]:
        if cost + w < dist[v]:
            dist[v] = cost + w
            heappush(pq, (dist[v], v))

print(dist[N + 1])
