
import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    if not data:
        return

    it = iter(data)
    E = int(next(it))
    R = int(next(it))

    adj = [[] for _ in range(E + 1)]
    for _ in range(R):
        A = int(next(it))
        B = int(next(it))
        C = int(next(it))
        adj[A].append((B, C))
        adj[B].append((A, C))

    K = int(next(it))

    queries = []
    for _ in range(K):
        X = int(next(it))
        T = int(next(it))
        queries.append((X, T))

    for X, T in queries:
        min_dist = -1
        visited = [False] * (E + 1)
        q = deque()
        q.append((X, 0))
        visited[X] = True

        while q:
            u, dist = q.popleft()
            if u == X and dist > 0:
                if min_dist == -1 or dist < min_dist:
                    min_dist = dist
                continue

            for v, c in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    q.append((v, dist + c))

        print(min_dist)

if __name__ == "__main__":
    main()
