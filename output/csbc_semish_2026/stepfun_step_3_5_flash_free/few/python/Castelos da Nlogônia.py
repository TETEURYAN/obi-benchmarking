import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [[] for _ in range(n+1)]
    for _ in range(n-1):
        u = int(next(it))
        v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)
    cores = [0] * (n+1)
    def bfs_path(start, end):
        visited = [False] * (n+1)
        parent = [-1] * (n+1)
        q = deque([start])
        visited[start] = True
        while q:
            u = q.popleft()
            if u == end:
                break
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    parent[v] = u
                    q.append(v)
        path = []
        cur = end
        while cur != -1:
            path.append(cur)
            cur = parent[cur]
        path.reverse()
        return path
    for _ in range(m):
        p = int(next(it))
        q = int(next(it))
        c = int(next(it))
        caminho = bfs_path(p, q)
        for no in caminho:
            cores[no] = c
    sys.stdout.write(' '.join(str(cores[i]) for i in range(1, n+1)))

if __name__ == "__main__":
    main()