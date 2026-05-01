import sys
from collections import deque

def main():
    input = sys.stdin.readline

    N, K1, K2, P = map(int, input().split())

    metro = [[] for _ in range(N + 1)]
    bus = [[] for _ in range(N + 1)]

    for _ in range(K1):
        u, v = map(int, input().split())
        metro[u].append(v)
        metro[v].append(u)

    for _ in range(K2):
        u, v = map(int, input().split())
        bus[u].append(v)
        bus[v].append(u)

    A, B = map(int, input().split())

    INF = 10**18
    dist = [[INF, INF] for _ in range(N + 1)]
    dq = deque()

    dist[A][0] = 1
    dist[A][1] = 1
    dq.append((A, 0))
    dq.append((A, 1))

    while dq:
        u, t = dq.popleft()
        d = dist[u][t]

        if t == 0:
            for v in metro[u]:
                if dist[v][0] > d:
                    dist[v][0] = d
                    dq.appendleft((v, 0))
            for v in bus[u]:
                if dist[v][1] > d + 1:
                    dist[v][1] = d + 1
                    dq.append((v, 1))
        else:
            for v in bus[u]:
                if dist[v][1] > d:
                    dist[v][1] = d
                    dq.appendleft((v, 1))
            for v in metro[u]:
                if dist[v][0] > d + 1:
                    dist[v][0] = d + 1
                    dq.append((v, 0))

    ans = min(dist[B][0], dist[B][1])
    if ans == INF:
        print(-1)
    else:
        print(ans * P)

if __name__ == "__main__":
    main()
