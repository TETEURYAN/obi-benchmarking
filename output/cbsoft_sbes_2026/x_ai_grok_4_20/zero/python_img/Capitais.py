
import sys
from collections import deque

sys.setrecursionlimit(200000)

N = int(input())
adj = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

leaves = [i for i in range(1, N + 1) if len(adj[i]) == 1]
if not leaves:
    print(0)
    sys.exit(0)

dist = [-1] * (N + 1)
q = deque()
for leaf in leaves:
    dist[leaf] = 0
    q.append(leaf)

while q:
    u = q.popleft()
    for v in adj[u]:
        if dist[v] == -1:
            dist[v] = dist[u] + 1
            q.append(v)

farthest = max(range(1, N + 1), key=lambda x: dist[x])
dist = [-1] * (N + 1)
q = deque([farthest])
dist[farthest] = 0
while q:
    u = q.popleft()
    for v in adj[u]:
        if dist[v] == -1:
            dist[v] = dist[u] + 1
            q.append(v)

diameter = max(dist[1:])
print((diameter + 2) // 3)
