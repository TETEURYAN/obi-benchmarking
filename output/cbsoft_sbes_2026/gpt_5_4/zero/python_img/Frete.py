import sys
import heapq

def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    adj = [[] for _ in range(N + 1)]
    
    for _ in range(M):
        A, B, C = map(int, input().split())
        adj[A].append((B, C))
        adj[B].append((A, C))
    
    INF = 10**18
    dist = [INF] * (N + 1)
    dist[1] = 0
    pq = [(0, 1)]
    
    while pq:
        d, u = heapq.heappop(pq)
        if d != dist[u]:
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
