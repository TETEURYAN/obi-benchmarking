import sys
from collections import deque

data = sys.stdin.read().split()
C = int(data[0])
tiles = [int(data[i+1]) for i in range(C)]

INF = float('inf')
dist = [INF] * C
dist[0] = 0
q = deque([0])

while q:
    u = q.popleft()
    for step in [1, 2]:
        v = u + step
        if v < C and tiles[v] == 1 and dist[v] == INF:
            dist[v] = dist[u] + 1
            q.append(v)

print(dist[C-1] if dist[C-1] != INF else -1)