
import sys
from collections import deque

sys.setrecursionlimit(200000)

N = int(input())
adj = [[] for _ in range(N+1)]
for _ in range(N-1):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

leaves = [i for i in range(1, N+1) if len(adj[i]) == 1]
if not leaves:
    print(0)
    sys.exit(0)

dist = [-1] * (N+1)
q = deque()
for leaf in leaves:
    dist[leaf] = 0
    q.append(leaf)

farthest = leaves[0]
while q:
    u = q.popleft()
    farthest = u
    for v in adj[u]:
        if dist[v] == -1:
            dist[v] = dist[u] + 1
            q.append(v)

dist = [-1] * (N+1)
q = deque([farthest])
dist[farthest] = 0
second = farthest
while q:
    u = q.popleft()
    second = u
    for v in adj[u]:
        if dist[v] == -1:
            dist[v] = dist[u] + 1
            q.append(v)

diameter = dist[second]
if diameter % 2 == 0:
    center = second
    for _ in range(diameter // 2):
        for nei in adj[center]:
            if dist[nei] == dist[center] - 1:
                center = nei
                break
    root = center
else:
    c1 = second
    for _ in range(diameter // 2):
        for nei in adj[c1]:
            if dist[nei] == dist[c1] - 1:
                c1 = nei
                break
    c2 = c1
    for nei in adj[c1]:
        if dist[nei] == dist[c1] + 1:
            c2 = nei
            break
    root = c1

parent = [-1] * (N+1)
depth = [0] * (N+1)
is_capital = [False] * (N+1)
q = deque([root])
parent[root] = root
while q:
    u = q.popleft()
    children = 0
    for v in adj[u]:
        if v != parent[u]:
            parent[v] = u
            depth[v] = depth[u] + 1
            q.append(v)
            children += 1
    if children == 0 and u != root:
        is_capital[u] = True
    if u == root and len(adj[u]) <= 1:
        is_capital[u] = True

capitals = [i for i in range(1, N+1) if is_capital[i]]

if len(capitals) <= 1:
    print(0)
    sys.exit(0)

def bfs_multi(starts):
    d = [-1] * (N+1)
    q = deque()
    for s in starts:
        d[s] = 0
        q.append(s)
    while q:
        u = q.popleft()
        for v in adj[u]:
            if d[v] == -1:
                d[v] = d[u] + 1
                q.append(v)
    return d

d_from_cap = bfs_multi(capitals)

min_dist = float('inf')
for c in capitals:
    for nei in adj[c]:
        if not is_capital[nei]:
            min_dist = min(min_dist, d_from_cap[nei] + 1)

if min_dist == float('inf'):
    min_dist = 1

print(min_dist)
