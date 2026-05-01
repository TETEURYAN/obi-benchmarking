
import sys
from collections import deque

def main():
    sys.setrecursionlimit(1 << 25)
    N = int(sys.stdin.readline())
    adj = [[] for _ in range(N+1)]
    for _ in range(N-1):
        u, v = map(int, sys.stdin.readline().split())
        adj[u].append(v)
        adj[v].append(u)

    leaves = []
    for i in range(1, N+1):
        if len(adj[i]) == 1:
            leaves.append(i)

    if len(leaves) == 2:
        print(1)
        return

    parent = [0]*(N+1)
    q = deque()
    for leaf in leaves:
        q.append(leaf)
        parent[leaf] = leaf

    while q:
        u = q.popleft()
        for v in adj[u]:
            if parent[v] == 0 and v != parent[u]:
                parent[v] = u
                q.append(v)

    max_dist = 0
    for leaf in leaves:
        dist = 0
        current = leaf
        while parent[current] != current:
            current = parent[current]
            dist += 1
        if dist > max_dist:
            max_dist = dist

    print(max_dist)

if __name__ == "__main__":
    main()
