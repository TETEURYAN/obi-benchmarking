
import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    idx = 0
    N = int(data[idx])
    A = int(data[idx+1])
    B = int(data[idx+2])
    idx += 3

    graph = [[] for _ in range(N+1)]
    for _ in range(N-1):
        P = int(data[idx])
        Q = int(data[idx+1])
        D = int(data[idx+2])
        idx += 3
        graph[P].append((Q, D))
        graph[Q].append((P, D))

    parent = [0] * (N+1)
    dist = [0] * (N+1)
    visited = [False] * (N+1)
    q = deque()
    q.append(A)
    visited[A] = True

    while q:
        u = q.popleft()
        for v, d in graph[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                dist[v] = dist[u] + d
                q.append(v)

    print(dist[B])

if __name__ == "__main__":
    main()
