import sys
import heapq

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    M = int(input_data[1])
    
    adj = [[] for _ in range(N + 1)]
    
    idx = 2
    for _ in range(M):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        c = int(input_data[idx+2])
        idx += 3
        adj[u].append((v, c))
        adj[v].append((u, c))
        
    dist = [float('inf')] * (N + 1)
    dist[1] = 0
    
    pq = [(0, 1)]
    
    while pq:
        d, u = heapq.heappop(pq)
        
        if d > dist[u]:
            continue
            
        if u == N:
            break
            
        for v, c in adj[u]:
            if dist[u] + c < dist[v]:
                dist[v] = dist[u] + c
                heapq.heappush(pq, (dist[v], v))
                
    print(dist[N])

if __name__ == '__main__':
    solve()