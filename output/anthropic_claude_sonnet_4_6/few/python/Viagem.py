import sys
import heapq

def solve():
    data = sys.stdin.read().split()
    idx = 0
    V = int(data[idx]); idx+=1
    N = int(data[idx]); idx+=1
    M = int(data[idx]); idx+=1
    
    adj = [[] for _ in range(N+1)]
    for _ in range(M):
        a = int(data[idx]); idx+=1
        b = int(data[idx]); idx+=1
        t = int(data[idx]); idx+=1
        p = int(data[idx]); idx+=1
        adj[a].append((b, t, p))
        adj[b].append((a, t, p))
    
    X = int(data[idx]); idx+=1
    Y = int(data[idx]); idx+=1
    
    if X == Y:
        print(0)
        return
    
    # Dijkstra with state (time, cost) - minimize time subject to cost <= V
    # dist[node][cost] = min time to reach node spending exactly 'cost'
    INF = float('inf')
    dist = [[INF] * (V+1) for _ in range(N+1)]
    dist[X][0] = 0
    
    # heap: (time, cost, node)
    heap = [(0, 0, X)]
    
    while heap:
        t, c, u = heapq.heappop(heap)
        if t > dist[u][c]:
            continue
        for v, et, ep in adj[u]:
            nc = c + ep
            nt = t + et
            if nc <= V and nt < dist[v][nc]:
                dist[v][nc] = nt
                heapq.heappush(heap, (nt, nc, v))
    
    ans = min(dist[Y][c] for c in range(V+1))
    if ans == INF:
        print(-1)
    else:
        print(ans)

solve()