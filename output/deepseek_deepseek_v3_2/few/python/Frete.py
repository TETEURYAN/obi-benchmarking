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
        a = int(next(it))
        b = int(next(it))
        c = int(next(it))
        adj[a].append((b, c))
        adj[b].append((a, c))
    
    INF = 10**9
    dist = [INF] * (N + 1)
    dist[1] = 0
    pq = [(0, 1)]
    
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        if u == N:
            break
        for v, w in adj[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))
    
    print(dist[N])

if __name__ == "__main__":
    main()