
import sys
import heapq

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    
    idx = 0
    N = int(data[idx])
    M = int(data[idx + 1])
    idx += 2
    
    adj = [[] for _ in range(N + 2)]
    
    for _ in range(M):
        S = int(data[idx])
        T = int(data[idx + 1])
        B = int(data[idx + 2])
        idx += 3
        adj[S].append((T, B))
        adj[T].append((S, B))
    
    dist = [float('inf')] * (N + 2)
    dist[0] = 0
    pq = [(0, 0)]
    
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        if u == N + 1:
            break
        for v, w in adj[u]:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))
    
    print(dist[N + 1])

solve()
