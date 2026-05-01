import heapq
import sys
input = sys.stdin.readline

def solve():
    line1 = input().split()
    V, N, M = int(line1[0]), int(line1[1]), int(line1[2])
    
    graph = [[] for _ in range(N + 1)]
    
    for _ in range(M):
        parts = input().split()
        a, b, t, p = int(parts[0]), int(parts[1]), int(parts[2]), int(parts[3])
        graph[a].append((b, t, p))
        graph[b].append((a, t, p))
    
    last_line = input().split()
    X, Y = int(last_line[0]), int(last_line[1])
    
    # Dijkstra with state (time, cost) - minimize time subject to cost <= V
    # dist[node][cost] = minimum time to reach node spending exactly 'cost'
    # We want min time over all costs <= V
    
    INF = float('inf')
    # dist[node][cost] = min time
    dist = [[INF] * (V + 1) for _ in range(N + 1)]
    dist[X][0] = 0
    
    # heap: (time, cost, node)
    heap = [(0, 0, X)]
    
    while heap:
        time, cost, node = heapq.heappop(heap)
        
        if time > dist[node][cost]:
            continue
        
        for neighbor, t, p in graph[node]:
            new_cost = cost + p
            new_time = time + t
            
            if new_cost > V:
                continue
            
            if new_time < dist[neighbor][new_cost]:
                dist[neighbor][new_cost] = new_time
                heapq.heappush(heap, (new_time, new_cost, neighbor))
    
    ans = min(dist[Y][c] for c in range(V + 1))
    
    if ans == INF:
        print(-1)
    else:
        print(ans)

solve()