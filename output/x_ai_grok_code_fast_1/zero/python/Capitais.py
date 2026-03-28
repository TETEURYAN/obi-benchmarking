
import sys
from collections import deque

input = sys.stdin.read
data = input().split()

N = int(data[0])
adj = [[] for _ in range(N + 1)]
degree = [0] * (N + 1)
index = 1
for i in range(N - 1):
    u = int(data[index])
    v = int(data[index + 1])
    adj[u].append(v)
    adj[v].append(u)
    degree[u] += 1
    degree[v] += 1
    index += 2

capitals = [i for i in range(1, N + 1) if degree[i] == 1]

dist = [-1] * (N + 1)
queue = deque()
for cap in capitals:
    dist[cap] = 0
    queue.append(cap)

min_dist = float('inf')
while queue:
    u = queue.popleft()
    for v in adj[u]:
        if dist[v] == -1:
            dist[v] = dist[u] + 1
            queue.append(v)
        else:
            min_dist = min(min_dist, dist[u] + 1 + dist[v])

print(min_dist)
