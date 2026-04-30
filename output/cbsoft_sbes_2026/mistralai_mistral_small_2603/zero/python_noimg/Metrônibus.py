
import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    it = iter(data)
    N = int(next(it)); K1 = int(next(it)); K2 = int(next(it)); P = int(next(it))

    graph = [[] for _ in range(N+1)]

    for _ in range(K1):
        u = int(next(it)); v = int(next(it))
        graph[u].append((v, 0))
        graph[v].append((u, 0))

    for _ in range(K2):
        u = int(next(it)); v = int(next(it))
        graph[u].append((v, 1))
        graph[v].append((u, 1))

    A = int(next(it)); B = int(next(it))

    INF = float('inf')
    dist = [[INF, INF] for _ in range(N+1)]
    dist[A][0] = 0
    dist[A][1] = 0

    q = deque()
    q.append((A, 0))
    q.append((A, 1))

    while q:
        u, system = q.popleft()
        for (v, edge_system) in graph[u]:
            if edge_system == system:
                if dist[v][system] > dist[u][system]:
                    dist[v][system] = dist[u][system]
                    q.appendleft((v, system))
            else:
                if dist[v][edge_system] > dist[u][system] + P:
                    dist[v][edge_system] = dist[u][system] + P
                    q.append((v, edge_system))

    ans = min(dist[B][0], dist[B][1])
    print(ans if ans != INF else -1)

if __name__ == '__main__':
    main()
