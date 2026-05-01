
import sys
from collections import deque

def main():
    sys.setrecursionlimit(1 << 25)
    n = int(sys.stdin.readline())
    adj = [[] for _ in range(n+1)]
    for _ in range(n-1):
        x, y = map(int, sys.stdin.readline().split())
        adj[x].append(y)
        adj[y].append(x)

    parent = [0] * (n+1)
    depth = [0] * (n+1)
    q = deque([1])
    parent[1] = -1
    while q:
        u = q.popleft()
        for v in adj[u]:
            if parent[v] == 0 and v != parent[u]:
                parent[v] = u
                depth[v] = depth[u] + 1
                q.append(v)

    max_depth = max(depth)
    u = depth.index(max_depth)
    depth = [0] * (n+1)
    parent = [0] * (n+1)
    q = deque([u])
    parent[u] = -1
    while q:
        node = q.popleft()
        for neighbor in adj[node]:
            if parent[neighbor] == 0 and neighbor != parent[node]:
                parent[neighbor] = node
                depth[neighbor] = depth[node] + 1
                q.append(neighbor)

    diameter = max(depth)
    v = depth.index(diameter)

    path = []
    current = v
    while current != -1:
        path.append(current)
        current = parent[current]

    max_cycle = 0
    count = 0
    m = len(path)

    for i in range(m):
        for j in range(i+1, m):
            dist = j - i + 1
            if dist > max_cycle:
                max_cycle = dist
                count = 1
            elif dist == max_cycle:
                count += 1

    print(max_cycle)
    print(count)

if __name__ == "__main__":
    main()
