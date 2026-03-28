
import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    if not data:
        return

    n = int(data[0])
    cards = list(map(int, data[1:n+1]))
    adj = [[] for _ in range(n+1)]
    idx = n + 1

    for _ in range(n-1):
        u = int(data[idx])
        v = int(data[idx+1])
        adj[u].append(v)
        adj[v].append(u)
        idx += 2

    pos = [[] for _ in range(n//2 + 1)]
    for i in range(n):
        num = cards[i]
        pos[num].append(i+1)

    total = 0
    parent = [0] * (n + 1)
    depth = [0] * (n + 1)

    def bfs(start):
        q = deque()
        q.append(start)
        parent[start] = -1
        depth[start] = 0
        visited = [False] * (n + 1)
        visited[start] = True
        while q:
            u = q.popleft()
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    parent[v] = u
                    depth[v] = depth[u] + 1
                    q.append(v)

    for num in range(1, n//2 + 1):
        u, v = pos[num]
        if depth[u] == 0 and depth[v] == 0:
            bfs(u)
        lca = u
        while depth[lca] > depth[v]:
            lca = parent[lca]
        while depth[v] > depth[lca]:
            v = parent[v]
        while lca != v:
            lca = parent[lca]
            v = parent[v]
        total += depth[u] + depth[u] - 2 * depth[lca]

    print(total)

if __name__ == "__main__":
    main()
