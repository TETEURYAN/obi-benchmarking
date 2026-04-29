import sys
import heapq

def main():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    adj = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        a, b, c = map(int, input().split())
        adj[a].append((b, c))
        adj[b].append((a, c))
    
    INF = 10**18
    dist = [INF] * (n + 1)
    dist[1] = 0
    pq = [(0, 1)]
    
    while pq:
        d, u = heapq.heappop(pq)
        if d != dist[u]:
            continue
        if u == n:
            break
        for v, w in adj[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))
    
    print(dist[n])

if __name__ == "__main__":
    main()