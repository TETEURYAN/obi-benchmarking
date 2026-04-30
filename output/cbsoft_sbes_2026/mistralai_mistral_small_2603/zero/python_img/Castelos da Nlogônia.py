
import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    graph = [[] for _ in range(n+1)]
    for _ in range(n-1):
        u = int(next(it))
        v = int(next(it))
        graph[u].append(v)
        graph[v].append(u)

    colors = [0] * (n+1)

    for _ in range(m):
        p = int(next(it))
        q = int(next(it))
        c = int(next(it))

        parent = [0] * (n+1)
        visited = [False] * (n+1)
        q_bfs = deque()
        q_bfs.append(p)
        visited[p] = True
        parent[p] = -1

        found = False
        while q_bfs and not found:
            u = q_bfs.popleft()
            for v in graph[u]:
                if not visited[v]:
                    visited[v] = True
                    parent[v] = u
                    q_bfs.append(v)
                    if v == q:
                        found = True
                        break
            if found:
                break

        path = []
        node = q
        while node != -1:
            path.append(node)
            node = parent[node]

        for node in path:
            colors[node] = c

    print(' '.join(map(str, colors[1:])))

if __name__ == '__main__':
    main()
