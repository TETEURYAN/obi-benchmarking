import sys
import heapq

sys.setrecursionlimit(200000)

def solve():
    data = sys.stdin.read().split()
    if not data:
        return

    iterator = iter(data)
    try:
        N = int(next(iterator))
        M = int(next(iterator))
    except StopIteration:
        return

    adj = [[] for _ in range(N + 1)]
    
    for _ in range(M):
        try:
            u = int(next(iterator))
            v = int(next(iterator))
            p = int(next(iterator))
            adj[u].append((v, p))
            adj[v].append((u, p))
        except StopIteration:
            break
            
    try:
        S = int(next(iterator))
    except StopIteration:
        return

    dist = [float('inf')] * (N + 1)
    dist[S] = 0
    pq = [(0, S)]
    
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in adj[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))
    
    min_ping = float('inf')
    max_ping = 0
    
    for i in range(1, N + 1):
        if i != S:
            if dist[i] < min_ping:
                min_ping = dist[i]
            if dist[i] > max_ping:
                max_ping = dist[i]
                
    print(max_ping - min_ping)

if __name__ == '__main__':
    solve()