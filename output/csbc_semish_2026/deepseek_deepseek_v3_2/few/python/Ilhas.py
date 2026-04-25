import sys
import heapq

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    M = int(next(it))
    
    adj = [[] for _ in range(N + 1)]
    for _ in range(M):
        u = int(next(it))
        v = int(next(it))
        p = int(next(it))
        adj[u].append((v, p))
        adj[v].append((u, p))
    S = int(next(it))
    
    INF = 10**18
    dist = [INF] * (N + 1)
    dist[S] = 0
    pq = [(0, S)]
    
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in adj[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))
    
    min_ping = INF
    max_ping = 0
    for i in range(1, N + 1):
        if i == S:
            continue
        if dist[i] < min_ping:
            min_ping = dist[i]
        if dist[i] > max_ping:
            max_ping = dist[i]
    
    print(max_ping - min_ping)

if __name__ == "__main__":
    main()