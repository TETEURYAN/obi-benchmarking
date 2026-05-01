
import sys
from heapq import heappush, heappop

input = sys.stdin.read
data = input().split()

index = 0
V = int(data[index]); index += 1
N = int(data[index]); index += 1
M = int(data[index]); index += 1

graph = [[] for _ in range(N+1)]
for _ in range(M):
    A = int(data[index]); index += 1
    B = int(data[index]); index += 1
    T = int(data[index]); index += 1
    P = int(data[index]); index += 1
    if P <= V:
        graph[A].append((B, T, P))
        graph[B].append((A, T, P))

X = int(data[index]); index += 1
Y = int(data[index]); index += 1

if X == Y:
    print(0)
    sys.exit(0)

INF = 10**18
dist = [[INF] * (V + 1) for _ in range(N + 1)]
dist[X][0] = 0

pq = []
heappush(pq, (0, X, 0))

while pq:
    time, u, spent = heappop(pq)
    if time > dist[u][spent]:
        continue
    for v, t, p in graph[u]:
        new_spent = spent + p
        if new_spent > V:
            continue
        new_time = time + t
        if new_time < dist[v][new_spent]:
            dist[v][new_spent] = new_time
            heappush(pq, (new_time, v, new_spent))

ans = min(dist[Y])
print(ans if ans < INF else -1)
