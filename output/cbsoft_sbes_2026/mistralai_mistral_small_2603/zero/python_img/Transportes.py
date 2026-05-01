
import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))

    prices = [0] * (k + 1)
    for i in range(1, k + 1):
        prices[i] = int(next(it))

    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        v = int(next(it))
        u = int(next(it))
        t = int(next(it))
        graph[v].append((u, t))
        graph[u].append((v, t))

    a = int(next(it))
    b = int(next(it))

    if a == b:
        print(0)
        return

    INF = float('inf')
    dist = [INF] * (n + 1)
    dist[a] = 0
    q = deque()
    q.append(a)

    while q:
        u = q.popleft()
        if u == b:
            break
        for (v, t) in graph[u]:
            new_cost = dist[u] + prices[t]
            if new_cost < dist[v]:
                dist[v] = new_cost
                q.append(v)

    print(dist[b] if dist[b] != INF else -1)

if __name__ == '__main__':
    main()
