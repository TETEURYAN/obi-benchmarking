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

def tree_center(adj):
    a, _ = bfs_farthest(1, adj)
    b, dist_a = bfs_farthest(a, adj)
    _, dist_b = bfs_farthest(b, adj)
    diameter_edges = dist_a[b]
    radius = (diameter_edges + 1) // 2
    for i in range(1, len(adj)):
        if max(dist_a[i], dist_b[i]) == radius:
            return i
    return 1

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    it = iter(data)
    N = next(it)
    M = next(it)

    adj1 = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        a = next(it)
        b = next(it)
        adj1[a].append(b)
        adj1[b].append(a)

    adj2 = [[] for _ in range(M + 1)]
    for _ in range(M - 1):
        x = next(it)
        y = next(it)
        adj2[x].append(y)
        adj2[y].append(x)

    c1 = tree_center(adj1)
    c2 = tree_center(adj2)
    print(c1, c2)

if __name__ == "__main__":
    main()
