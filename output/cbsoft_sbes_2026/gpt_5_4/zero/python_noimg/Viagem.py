import sys
import heapq

def main():
    input = sys.stdin.readline
    V, N, M = map(int, input().split())
    
    adj = [[] for _ in range(N + 1)]
    for _ in range(M):
        a, b, t, p = map(int, input().split())
        adj[a].append((b, t, p))
        adj[b].append((a, t, p))
    
    X, Y = map(int, input().split())
    
    INF = 10**18
    dist = [[INF] * (V + 1) for _ in range(N + 1)]
    dist[X][0] = 0
    
    pq = [(0, X, 0)]  # tempo, nó, custo_gasto
    
    while pq:
        tempo, u, custo = heapq.heappop(pq)
        if tempo != dist[u][custo]:
            continue
        
        for v, t, p in adj[u]:
            nc = custo + p
            if nc <= V:
                nt = tempo + t
                if nt < dist[v][nc]:
                    dist[v][nc] = nt
                    heapq.heappush(pq, (nt, v, nc))
    
    ans = min(dist[Y])
    print(ans if ans < INF else -1)

if __name__ == "__main__":
    main()
