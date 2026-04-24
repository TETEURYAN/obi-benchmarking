
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

    parent = [0] * (n + 1)
    depth = [0] * (n + 1)
    q = deque([1])
    parent[1] = 1
    depth[1] = 0
    while q:
        u = q.popleft()
        for v in adj[u]:
            if parent[v] == 0 and v != parent[u]:
                parent[v] = u
                depth[v] = depth[u] + 1
                q.append(v)

    max_depth = max(depth[1:])
    diameter_nodes = [i for i in range(1, n + 1) if depth[i] == max_depth]

    def bfs(start):
        dist = [-1] * (n + 1)
        q = deque([start])
        dist[start] = 0
        while q:
            u = q.popleft()
            for v in adj[u]:
                if dist[v] == -1:
                    dist[v] = dist[u] + 1
                    q.append(v)
        return dist

    if len(diameter_nodes) == 1:
        u = diameter_nodes[0]
        dist_u = bfs(u)
        max_dist = max(dist_u[1:])
        diameter = max_dist + 1
        count = 0
        for v in range(1, n + 1):
            if dist_u[v] == max_dist:
                count += 1
        print(diameter)
        print(count * (count - 1) // 2)
    else:
        u, v = diameter_nodes
        dist_u = bfs(u)
        dist_v = bfs(v)
        diameter = dist_u[v] + 1
        count = 0
        for node in range(1, n + 1):
            if dist_u[node] + dist_v[node] == dist_u[v]:
                count += 1
        print(diameter)
        print(count * (count - 1) // 2)

if __name__ == "__main__":
    main()
