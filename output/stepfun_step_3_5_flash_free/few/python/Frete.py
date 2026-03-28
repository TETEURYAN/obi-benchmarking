import sys
import heapq

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [[] for _ in range(n+1)]
    for _ in range(m):
        a = int(next(it))
        b = int(next(it))
        c = int(next(it))
        adj[a].append((b, c))
        adj[b].append((a, c))
    
    INF = 10**18
    dist = [INF] * (n+1)
    dist[1] = 0
    heap = [(0, 1)]
    
    while heap:
        d, u = heapq.heappop(heap)
        if d != dist[u]:
            continue
        if u == n:
            break
        for v, w in adj[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(heap, (nd, v))
    
    print(dist[n])

if __name__ == "__main__":
    main()