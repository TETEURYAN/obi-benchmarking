
import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    it = iter(data)
    N = int(next(it)); M = int(next(it)); K = int(next(it))
    P = [0] * (K + 1)
    for i in range(1, K + 1):
        P[i] = int(next(it))

    graph = [[] for _ in range(N + 1)]
    for _ in range(M):
        v = int(next(it)); u = int(next(it)); t = int(next(it))
        graph[v].append((u, t))
        graph[u].append((v, t))

    A = int(next(it)); B = int(next(it))

    INF = float('inf')
    dist = [INF] * (N + 1)
    dist[A] = 0
    q = deque()
    q.append(A)

    while q:
        u = q.popleft()
        if u == B:
            break
        for (v, t) in graph[u]:
            if dist[v] > dist[u] + P[t]:
                dist[v] = dist[u] + P[t]
                q.append(v)

    print(dist[B] if dist[B] != INF else -1)

if __name__ == '__main__':
    main()
