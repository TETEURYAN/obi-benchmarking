import sys
from collections import deque

def bfs_farthest(start, adj):
    n = len(adj) - 1
    dist = [-1] * (n + 1)
    q = deque([start])
    dist[start] = 0
    far = start
    while q:
        u = q.popleft()
        if dist[u] > dist[far]:
            far = u
        for v in adj[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                q.append(v)
    return far, dist

def find_center(adj):
    a, _ = bfs_farthest(1, adj)
    b, dist_a = bfs_farthest(a, adj)
    _, dist_b = bfs_farthest(b, adj)
    diameter_edges = dist_a[b]
    radius = (diameter_edges + 1) // 2
    for i in range(1, len(adj)):
        if max(dist_a[i], dist_b[i]) == radius:
            return i
    return 1

data = list(map(int, sys.stdin.read().split()))
if not data:
    sys.exit()

n, m = data[0], data[1]
idx = 2

adj1 = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u = data[idx]
    v = data[idx + 1]
    idx += 2
    adj1[u].append(v)
    adj1[v].append(u)

adj2 = [[] for _ in range(m + 1)]
for _ in range(m - 1):
    u = data[idx]
    v = data[idx + 1]
    idx += 2
    adj2[u].append(v)
    adj2[v].append(u)

c1 = find_center(adj1)
c2 = find_center(adj2)

print(c1, c2)