
import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    if not data:
        print(-1)
        return

    it = iter(data)
    N = int(next(it))
    K1 = int(next(it))
    K2 = int(next(it))
    P = int(next(it))

    adj_metro = [[] for _ in range(N + 1)]
    adj_onibus = [[] for _ in range(N + 1)]

    for _ in range(K1):
        u = int(next(it))
        v = int(next(it))
        adj_metro[u].append(v)
        adj_metro[v].append(u)

    for _ in range(K2):
        u = int(next(it))
        v = int(next(it))
        adj_onibus[u].append(v)
        adj_onibus[v].append(u)

    A = int(next(it))
    B = int(next(it))

    if A == B:
        print(0)
        return

    INF = float('inf')
    dist_metro = [INF] * (N + 1)
    dist_onibus = [INF] * (N + 1)
    dist_metro[A] = 0
    dist_onibus[A] = 0

    q = deque()
    q.append((A, 0))
    q.append((A, 1))

    while q:
        u, system = q.popleft()
        current_dist = dist_metro[u] if system == 0 else dist_onibus[u]

        if system == 0:
            for v in adj_metro[u]:
                if dist_metro[v] > current_dist:
                    dist_metro[v] = current_dist
                    q.appendleft((v, 0))
            for v in adj_onibus[u]:
                if dist_onibus[v] > current_dist + P:
                    dist_onibus[v] = current_dist + P
                    q.append((v, 1))
        else:
            for v in adj_onibus[u]:
                if dist_onibus[v] > current_dist:
                    dist_onibus[v] = current_dist
                    q.appendleft((v, 1))
            for v in adj_metro[u]:
                if dist_metro[v] > current_dist + P:
                    dist_metro[v] = current_dist + P
                    q.append((v, 0))

    min_dist = min(dist_metro[B], dist_onibus[B])
    print(min_dist if min_dist != INF else -1)

if __name__ == "__main__":
    main()
