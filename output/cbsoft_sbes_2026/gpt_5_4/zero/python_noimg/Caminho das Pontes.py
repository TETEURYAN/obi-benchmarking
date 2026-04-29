import sys
import heapq

def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    total = N + 2

    adj = [[] for _ in range(total)]
    for _ in range(M):
        s, t, b = map(int, input().split())
        adj[s].append((t, b))
        adj[t].append((s, b))

    INF = 10**18
    dist = [INF] * total
    dist[0] = 0
    pq = [(0, 0)]

    while pq:
        d, u = heapq.heappop(pq)
        if d != dist[u]:
            continue
        if u == N + 1:
            break
        for v, w in adj[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))

    print(dist[N + 1])

if __name__ == "__main__":
    main()
