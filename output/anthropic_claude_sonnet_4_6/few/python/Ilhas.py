import sys
import heapq

def main():
    data = sys.stdin.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(data[idx]); idx += 1
        v = int(data[idx]); idx += 1
        p = int(data[idx]); idx += 1
        adj[u].append((v, p))
        adj[v].append((u, p))
    
    s = int(data[idx]); idx += 1
    
    INF = float('inf')
    dist = [INF] * (n + 1)
    dist[s] = 0
    heap = [(0, s)]
    
    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue
        for v, w in adj[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(heap, (nd, v))
    
    other_dists = [dist[i] for i in range(1, n + 1) if i != s]
    print(max(other_dists) - min(other_dists))

main()