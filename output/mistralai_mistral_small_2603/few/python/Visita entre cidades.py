
import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    if not data:
        return

    idx = 0
    N = int(data[idx])
    A = int(data[idx+1])
    B = int(data[idx+2])
    idx += 3

    adj = [[] for _ in range(N+1)]
    for _ in range(N-1):
        P = int(data[idx])
        Q = int(data[idx+1])
        D = int(data[idx+2])
        adj[P].append((Q, D))
        adj[Q].append((P, D))
        idx += 3

    if A == B:
        print(0)
        return

    parent = [0] * (N + 1)
    depth = [-1] * (N + 1)
    distance_from_root = [0] * (N + 1)
    q = deque()
    q.append(A)
    depth[A] = 0
    parent[A] = A

    while q:
        u = q.popleft()
        for v, d in adj[u]:
            if depth[v] == -1:
                depth[v] = depth[u] + 1
                parent[v] = u
                distance_from_root[v] = distance_from_root[u] + d
                q.append(v)

    lca = B
    while lca != parent[lca]:
        lca = parent[lca]

    distance = distance_from_root[B] - 2 * distance_from_root[lca] + distance_from_root[A]
    print(distance)

if __name__ == "__main__":
    main()
