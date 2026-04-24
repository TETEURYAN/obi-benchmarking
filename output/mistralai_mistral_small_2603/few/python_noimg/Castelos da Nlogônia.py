
import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    if not data:
        return

    idx = 0
    N = int(data[idx])
    M = int(data[idx+1])
    idx += 2

    adj = [[] for _ in range(N+1)]
    for _ in range(N-1):
        u = int(data[idx])
        v = int(data[idx+1])
        adj[u].append(v)
        adj[v].append(u)
        idx += 2

    parent = [0] * (N + 1)
    depth = [0] * (N + 1)
    q = deque([1])
    parent[1] = 1
    while q:
        u = q.popleft()
        for v in adj[u]:
            if parent[v] == 0 and v != parent[u]:
                parent[v] = u
                depth[v] = depth[u] + 1
                q.append(v)

    colors = [0] * (N + 1)

    for _ in range(M):
        P = int(data[idx])
        Q = int(data[idx+1])
        C = int(data[idx+2])
        idx += 3

        path = set()
        u, v = P, Q
        while u != v:
            if depth[u] > depth[v]:
                path.add(u)
                u = parent[u]
            else:
                path.add(v)
                v = parent[v]
        path.add(u)

        for node in path:
            colors[node] = C

    print(' '.join(map(str, colors[1:N+1])))

if __name__ == '__main__':
    main()
