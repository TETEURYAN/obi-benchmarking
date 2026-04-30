import heapq
import sys
input = sys.stdin.readline

def solve():
    line1 = input().split()
    V, N, M = int(line1[0]), int(line1[1]), int(line1[2])
    
    # adjacency list: adj[u] = list of (v, time, cost)
    adj = [[] for _ in range(N + 1)]
    
    for _ in range(M):
        parts = input().split()
        a, b, t, p = int(parts[0]), int(parts[1]), int(parts[2]), int(parts[3])
        adj[a].append((b, t, p))
        adj[b].append((a, t, p))
    
    last_line = input().split()
    X, Y = int(last_line[0]), int(last_line[1])
    
    if X == Y:
        print(0)
        return
    
    # Dijkstra with state (node, cost_spent)
    # We want minimum time to reach Y with total cost <= V
    # dist[node][cost] = minimum time to reach node spending exactly 'cost'
    
    INF = float('inf')
    # dist[node][cost] = min time
    dist = [[INF] * (V + 1) for _ in range(N + 1)]
    dist[X][0] = 0
    
    # priority queue: (time, node, cost_spent)
    pq = [(0, X, 0)]
    
    while pq:
        time, u, cost = heapq.heappop(pq)
        
        if time > dist[u][cost]:
            continue
        
        if u == Y:
            print(time)
            return
        
        for v, t, p in adj[u]:
            new_cost = cost + p
            new_time = time + t
            if new_cost <= V:
                if new_time < dist[v][new_cost]:
                    dist[v][new_cost] = new_time
                    heapq.heappush(pq, (new_time, v, new_cost))
    
    # Check if Y is reachable
    best = INF
    for c in range(V + 1):
        if dist[Y][c] < best:
            best = dist[Y][c]
    
    if best == INF:
        print(-1)
    else:
        print(best)

solve()