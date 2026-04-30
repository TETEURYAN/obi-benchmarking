
import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    it = iter(data)
    N = int(next(it))
    M = int(next(it))
    graph = [[] for _ in range(N+1)]
    for _ in range(N-1):
        u = int(next(it))
        v = int(next(it))
        graph[u].append(v)
        graph[v].append(u)

    parent = [0] * (N+1)
    depth = [0] * (N+1)
    stack = [1]
    parent[1] = -1
    while stack:
        u = stack.pop()
        for v in graph[u]:
            if parent[v] == 0 and v != parent[u]:
                parent[v] = u
                depth[v] = depth[u] + 1
                stack.append(v)

    colors = [0] * (N+1)

    for _ in range(M):
        p = int(next(it))
        q = int(next(it))
        c = int(next(it))

        path = set()
        a, b = p, q
        while a != b:
            if depth[a] > depth[b]:
                path.add(a)
                a = parent[a]
            else:
                path.add(b)
                b = parent[b]
        path.add(a)

        for node in path:
            colors[node] = c

    print(' '.join(map(str, colors[1:N+1])))

if __name__ == '__main__':
    main()
