
import sys
from collections import deque

def main():
    sys.setrecursionlimit(1 << 25)
    n = int(sys.stdin.readline())
    adj = [[] for _ in range(n+1)]
    for _ in range(n-1):
        a, b = map(int, sys.stdin.readline().split())
        adj[a].append(b)
        adj[b].append(a)

    parent = [0]*(n+1)
    size = [1]*(n+1)
    q = deque([1])
    parent[1] = -1
    order = []
    while q:
        u = q.popleft()
        order.append(u)
        for v in adj[u]:
            if parent[v] == 0 and v != parent[u]:
                parent[v] = u
                q.append(v)

    for u in reversed(order):
        if parent[u] != -1:
            size[parent[u]] += size[u]

    min_diff = float('inf')
    for u in range(2, n+1):
        diff = abs(n - 2*size[u])
        if diff < min_diff:
            min_diff = diff

    print(min_diff)

if __name__ == "__main__":
    main()
