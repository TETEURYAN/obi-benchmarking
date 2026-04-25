import sys
from collections import deque

def find_path(adj, start, end, n):
    parent = [-1] * (n + 1)
    visited = [False] * (n + 1)
    visited[start] = True
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node == end:
            break
        for neighbor in adj[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                parent[neighbor] = node
                queue.append(neighbor)
    path = []
    cur = end
    while cur != -1:
        path.append(cur)
        cur = parent[cur]
    return path

data = sys.stdin.read().split()
idx = 0
n = int(data[idx]); idx += 1
m = int(data[idx]); idx += 1

adj = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u = int(data[idx]); idx += 1
    v = int(data[idx]); idx += 1
    adj[u].append(v)
    adj[v].append(u)

color = [0] * (n + 1)

for _ in range(m):
    p = int(data[idx]); idx += 1
    q = int(data[idx]); idx += 1
    c = int(data[idx]); idx += 1
    path = find_path(adj, p, q, n)
    for node in path:
        color[node] = c

print(*color[1:])