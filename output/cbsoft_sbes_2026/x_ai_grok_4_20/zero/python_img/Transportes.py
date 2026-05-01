
import sys
from heapq import heappush, heappop
from collections import defaultdict

input = sys.stdin.read
data = input().split()

index = 0
N = int(data[index]); index += 1
M = int(data[index]); index += 1
K = int(data[index]); index += 1

P = [0] * (K + 1)
for i in range(1, K + 1):
    P[i] = int(data[index]); index += 1

graph = [defaultdict(list) for _ in range(N + 1)]
for _ in range(M):
    v = int(data[index]); index += 1
    u = int(data[index]); index += 1
    t = int(data[index]); index += 1
    graph[v][t].append(u)
    graph[u][t].append(v)

A = int(data[index]); index += 1
B = int(data[index])

if A == B:
    print(0)
    sys.exit()

INF = 10**18
dist = [[INF] * (K + 1) for _ in range(N + 1)]
for i in range(K + 1):
    dist[A][i] = 0

pq = []
for c in range(1, K + 1):
    if graph[A][c]:
        heappush(pq, (P[c], A, c))
        dist[A][c] = P[c]

while pq:
    cost, u, color = heappop(pq)
    if cost > dist[u][color]:
        continue
    if u == B:
        print(cost)
        sys.exit()
    
    for v in graph[u][color]:
        if cost < dist[v][color]:
            dist[v][color] = cost
            heappush(pq, (cost, v, color))
    
    for nc in range(1, K + 1):
        if nc == color:
            continue
        if not graph[u][nc]:
            continue
        new_cost = cost + P[nc]
        if new_cost < dist[u][nc]:
            dist[u][nc] = new_cost
            heappush(pq, (new_cost, u, nc))

ans = min(dist[B][1:])
print(ans if ans < INF else -1)
