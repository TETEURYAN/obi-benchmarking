
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
    parent[1] = 1
    while q:
        u = q.popleft()
        for v in adj[u]:
            if parent[v] == 0 and v != parent[u]:
                parent[v] = u
                depth[v] = depth[u] + 1
                q.append(v)

    max_depth = max(depth)
    diameter = []
    u = depth.index(max_depth)
    v = u
    while v != 1:
        diameter.append(v)
        v = parent[v]
    diameter.append(1)
    diameter = diameter[::-1]

    if len(diameter) == n:
        print(n)
        print(1)
        return

    max_len = 0
    count = 0
    for i in range(len(diameter)-1):
        u = diameter[i]
        v = diameter[i+1]
        current_len = depth[u] + depth[v] - 2 * depth[parent[u]]
        if current_len > max_len:
            max_len = current_len
            count = 0
        if current_len == max_len:
            count += 1

    print(max_len + 1)
    print(count)

if __name__ == "__main__":
    main()
