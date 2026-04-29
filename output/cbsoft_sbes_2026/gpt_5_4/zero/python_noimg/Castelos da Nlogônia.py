import sys
from collections import deque

def find_path(adj, start, end, n):
    parent = [-1] * (n + 1)
    q = deque([start])
    parent[start] = 0

    while q:
        u = q.popleft()
        if u == end:
            break
        for v in adj[u]:
            if parent[v] == -1:
                parent[v] = u
                q.append(v)

    path = []
    cur = end
    while cur != 0:
        path.append(cur)
        if cur == start:
            break
        cur = parent[cur]
    path.reverse()
    return path

def main():
    input = sys.stdin.readline
    n, m = map(int, input().split())

    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)

    color = [0] * (n + 1)

    for _ in range(m):
        p, q, c = map(int, input().split())
        path = find_path(adj, p, q, n)
        for node in path:
            color[node] = c

    print(*color[1:])

if __name__ == "__main__":
    main()
