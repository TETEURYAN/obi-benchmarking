import sys
import heapq

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    V = int(next(it))
    N = int(next(it))
    M = int(next(it))
    adj = [[] for _ in range(N+1)]
    for _ in range(M):
        a = int(next(it)); b = int(next(it)); t = int(next(it)); p = int(next(it))
        adj[a].append((b, t, p))
        adj[b].append((a, t, p))
    X = int(next(it)); Y = int(next(it))
    
    INF = 10**18
    dist = [[INF] * (V+1) for _ in range(N+1)]
    dist[X][0] = 0
    heap = [(0, X, 0)]
    
    while heap:
        t, u, c = heapq.heappop(heap)
        if t != dist[u][c]:
            continue
        if u == Y:
            print(t)
            return
        for v, t_edge, p_edge in adj[u]:
            nc = c + p_edge
            if nc <= V:
                nt = t + t_edge
                if nt < dist[v][nc]:
                    dist[v][nc] = nt
                    heapq.heappush(heap, (nt, v, nc))
    print(-1)

if __name__ == "__main__":
    main()