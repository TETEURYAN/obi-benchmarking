import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    if not data:
        return

    n = int(data[0])
    adj = [[] for _ in range(n + 1)]
    idx = 1
    for _ in range(n - 1):
        u = int(data[idx])
        v = int(data[idx + 1])
        adj[u].append(v)
        adj[v].append(u)
        idx += 2

    leaves = []
    degree = [0] * (n + 1)
    for i in range(1, n + 1):
        degree[i] = len(adj[i])
        if degree[i] == 1:
            leaves.append(i)

    capitals = []
    for i in range(1, n + 1):
        if degree[i] == 1:
            capitals.append(i)

    if len(capitals) == 2:
        print(1)
        return

    q = deque()
    dist = [-1] * (n + 1)
    for leaf in leaves:
        dist[leaf] = 0
        q.append(leaf)

    while q:
        u = q.popleft()
        for v in adj[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                q.append(v)

    max_dist = 0
    for capital in capitals:
        if dist[capital] > max_dist:
            max_dist = dist[capital]

    print(max_dist)

if __name__ == "__main__":
    main()