
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

    if A == B:
        print(0)
        return

    INF = 10**18
    dist = [[INF, INF] for _ in range(N+1)]
    dist[A][0] = 0
    dist[A][1] = 0

    q = deque()
    q.append((A, 0))
    q.append((A, 1))

    while q:
        u, last_transport = q.popleft()
        for (v, transport) in graph[u]:
            cost = 0 if transport == last_transport else P
            if dist[v][transport] > dist[u][last_transport] + cost:
                dist[v][transport] = dist[u][last_transport] + cost
                q.append((v, transport))

    ans = min(dist[B][0], dist[B][1])
    print(ans if ans != INF else -1)

if __name__ == "__main__":
    main()
