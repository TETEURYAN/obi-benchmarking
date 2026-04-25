import sys
import heapq

def main():
    data = sys.stdin.read().split()
    idx = 0
    N = int(data[idx]); idx += 1
    M = int(data[idx]); idx += 1
    
    # Nodes: 0 to N+1
    adj = [[] for _ in range(N + 2)]
    
    for _ in range(M):
        s = int(data[idx]); idx += 1
        t = int(data[idx]); idx += 1
        b = int(data[idx]); idx += 1
        adj[s].append((t, b))
        adj[t].append((s, b))
    
    # Dijkstra from 0 to N+1
    dist = [float('inf')] * (N + 2)
    dist[0] = 0
    pq = [(0, 0)]
    
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in adj[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))
    
    print(dist[N + 1])

main()