
import sys
sys.setrecursionlimit(200000)

def dfs(u, parent):
    stack = [(u, parent)]
    while stack:
        u, parent = stack.pop()
        for v in graph[u]:
            if v != parent:
                stack.append((v, u))
        size[u] = 1
        for v in graph[u]:
            if v != parent:
                size[u] += size[v]
                if size[v] > size[graph[u][0]]:
                    graph[u][0], graph[u][-1] = graph[u][-1], graph[u][0]

def centroid(u, parent, n):
    for v in graph[u]:
        if v != parent and size[v] > n // 2:
            return centroid(v, u, n)
    return u

def solve():
    n = int(sys.stdin.readline())
    global graph, size
    graph = [[] for _ in range(n + 1)]
    size = [0] * (n + 1)

    for _ in range(n - 1):
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)

    dfs(1, 0)
    c = centroid(1, 0, n)

    deg = [len(graph[i]) for i in range(1, n + 1)]
    capitals = [i for i in range(1, n + 1) if deg[i - 1] == 1]

    def bfs(start):
        dist = [-1] * (n + 1)
        dist[start] = 0
        q = [start]
        while q:
            u = q.pop()
            for v in graph[u]:
                if dist[v] == -1:
                    dist[v] = dist[u] + 1
                    q.append(v)
        return dist

    dist_from_c = bfs(c)

    min_dist = float('inf')
    for cap in capitals:
        if cap != c:
            for other in capitals:
                if other != cap:
                    d = dist_from_c[cap] + dist_from_c[other]
                    if d < min_dist:
                        min_dist = d

    print(min_dist)

if __name__ == "__main__":
    solve()
