
import sys
from collections import deque

input = sys.stdin.read
data = input().split()

N = int(data[0])
M = int(data[1])

graph = [[] for _ in range(N + 2)]
for i in range(M):
    s = int(data[2 + 3 * i])
    t = int(data[3 + 3 * i])
    b = int(data[4 + 3 * i])
    graph[s].append((t, b))
    graph[t].append((s, b))

INF = 10**9
dist = [INF] * (N + 2)
dist[0] = 0

q = deque([0])

while q:
    u = q.popleft()
    for v, b in graph[u]:
        if dist[v] > dist[u] + b:
            dist[v] = dist[u] + b
            if b == 0:
                q.appendleft(v)
            else:
                q.append(v)

print(dist[N + 1])
