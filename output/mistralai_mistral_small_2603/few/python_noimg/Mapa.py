
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
        a = int(data[idx])
        b = int(data[idx + 1])
        c = int(data[idx + 2])
        adj[a].append((b, c))
        adj[b].append((a, c))
        idx += 3

    total_pairs = n * (n - 1) // 2
    white_edges = 0
    for u in range(1, n + 1):
        for (v, c) in adj[u]:
            if v > u and c == 1:
                white_edges += 1

    if white_edges == 0:
        print(0)
        return

    subtree_sizes = [0] * (n + 1)
    visited = [False] * (n + 1)
    stack = [(1, None, False)]

    while stack:
        u, parent, processed = stack.pop()
        if not processed:
            stack.append((u, parent, True))
            visited[u] = True
            for (v, c) in adj[u]:
                if v != parent and not visited[v]:
                    stack.append((v, u, False))
        else:
            subtree_sizes[u] = 1
            for (v, c) in adj[u]:
                if v != parent:
                    subtree_sizes[u] += subtree_sizes[v]

    result = 0
    for u in range(1, n + 1):
        for (v, c) in adj[u]:
            if v > u and c == 1:
                result += subtree_sizes[v] * (n - subtree_sizes[v])

    print(result)

if __name__ == "__main__":
    main()
