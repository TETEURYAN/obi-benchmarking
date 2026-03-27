
import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    if not data:
        print(-1)
        return

    it = iter(data)
    N = int(next(it)); M = int(next(it)); K = int(next(it))
    P = [0] * (K + 1)
    for i in range(1, K + 1):
        P[i] = int(next(it))

    adj = [[] for _ in range(N + 1)]
    for _ in range(M):
        v = int(next(it)); u = int(next(it)); t = int(next(it))
        adj[v].append((u, t))
        adj[u].append((v, t))

    A = int(next(it)); B = int(next(it))

    if A == B:
        print(0)
        return

    INF = float('inf')
    dist = [[INF] * (K + 1) for _ in range(N + 1)]
    q = deque()

    for t in range(1, K + 1):
        dist[A][t] = P[t]
        q.append((A, t, P[t]))

    while q:
        u, t, cost = q.popleft()
        if cost > dist[u][t]:
            continue
        for (v, new_t) in adj[u]:
            new_cost = cost
            if new_t != t:
                new_cost += P[new_t]
            if new_cost < dist[v][new_t]:
                dist[v][new_t] = new_cost
                q.append((v, new_t, new_cost))

    ans = min(dist[B][t] for t in range(1, K + 1))
    print(ans if ans != INF else -1)

if __name__ == "__main__":
    main()
