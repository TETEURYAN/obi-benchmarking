import sys
from collections import deque

data = list(map(int, sys.stdin.read().split()))
if not data:
    sys.exit()

n = data[0]
adj = [[] for _ in range(n + 1)]
idx = 1
for _ in range(n - 1):
    u = data[idx]
    v = data[idx + 1]
    idx += 2
    adj[u].append(v)
    adj[v].append(u)

def bfs_far(start):
    dist = [-1] * (n + 1)
    parent = [0] * (n + 1)
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
                parent[v] = u
                q.append(v)
    return far, dist, parent

a, _, _ = bfs_far(1)
b, dist_a, parent = bfs_far(a)
diam_edges = dist_a[b]

path = []
cur = b
while cur:
    path.append(cur)
    if cur == a:
        break
    cur = parent[cur]
path.reverse()

diam_nodes = diam_edges + 1

on_diam = [False] * (n + 1)
for x in path:
    on_diam[x] = True

if diam_edges % 2 == 0:
    center = path[diam_edges // 2]
    target = diam_edges // 2

    count = 0
    seen = 0

    for nei in adj[center]:
        if on_diam[nei]:
            if dist_a[nei] < dist_a[center]:
                continue
        q = deque([(nei, center, 1)])
        c = 0
        while q:
            u, p, d = q.popleft()
            if d == target:
                c += 1
                continue
            for v in adj[u]:
                if v != p:
                    q.append((v, u, d + 1))
        count += seen * c
        seen += c

    ways = count
else:
    c1 = path[diam_edges // 2]
    c2 = path[diam_edges // 2 + 1]
    target = diam_edges // 2

    def count_side(start, blocked):
        q = deque([(start, blocked, 0)])
        c = 0
        while q:
            u, p, d = q.popleft()
            if d == target:
                c += 1
                continue
            for v in adj[u]:
                if v != p:
                    q.append((v, u, d + 1))
        return c

    cnt1 = count_side(c1, c2)
    cnt2 = count_side(c2, c1)
    ways = cnt1 * cnt2

print(diam_nodes)
print(ways)