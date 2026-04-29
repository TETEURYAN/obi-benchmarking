import sys
from collections import deque

def tree_center(adj):
    n = len(adj) - 1
    parent = [-1] * (n + 1)
    dist = [-1] * (n + 1)

    def bfs(start):
        for i in range(1, n + 1):
            dist[i] = -1
        q = deque([start])
        dist[start] = 0
        parent[start] = -1
        far = start
        while q:
            u = q.popleft()
            far = u
            for v in adj[u]:
                if dist[v] == -1:
                    dist[v] = dist[u] + 1
                    parent[v] = u
                    q.append(v)
        return far

    a = bfs(1)
    b = bfs(a)

    path = []
    cur = b
    while cur != -1:
        path.append(cur)
        cur = parent[cur]
    path.reverse()

    return path[len(path) // 2]

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    it = iter(data)
    n = next(it)
    m = next(it)

    adj1 = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        a = next(it)
        b = next(it)
        adj1[a].append(b)
        adj1[b].append(a)

    adj2 = [[] for _ in range(m + 1)]
    for _ in range(m - 1):
        x = next(it)
        y = next(it)
        adj2[x].append(y)
        adj2[y].append(x)

    c1 = tree_center(adj1)
    c2 = tree_center(adj2)

    print(c1, c2)

if __name__ == "__main__":
    main()
