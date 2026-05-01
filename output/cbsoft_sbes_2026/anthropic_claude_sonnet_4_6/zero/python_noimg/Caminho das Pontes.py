import heapq
import sys

def solve():
    input_data = sys.stdin.read().split()
    idx = 0
    N = int(input_data[idx]); idx += 1
    M = int(input_data[idx]); idx += 1
    
    # Node 0 = start, Node N+1 = end
    graph = [[] for _ in range(N + 2)]
    
    for _ in range(M):
        s = int(input_data[idx]); idx += 1
        t = int(input_data[idx]); idx += 1
        b = int(input_data[idx]); idx += 1
        graph[s].append((t, b))
        graph[t].append((s, b))
    
    # Dijkstra from 0 to N+1
    dist = [float('inf')] * (N + 2)
    dist[0] = 0
    pq = [(0, 0)]
    
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))
    
    print(dist[N + 1])

solve()