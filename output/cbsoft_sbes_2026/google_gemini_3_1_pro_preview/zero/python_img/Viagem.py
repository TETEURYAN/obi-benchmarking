
import sys
import heapq

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    V = int(input_data[0])
    N = int(input_data[1])
    M = int(input_data[2])
    
    adj = [[] for _ in range(N + 1)]
    
    idx = 3
    for _ in range(M):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        t = int(input_data[idx+2])
        p = int(input_data[idx+3])
        idx += 4
        adj[u].append((v, t, p))
        adj[v].append((u, t, p))
        
    X = int(input_data[idx])
    Y = int(input_data[idx+1])
    
    best_time = [[float('inf')] * (V + 1) for _ in range(N + 1)]
    min_cost = [float('inf')] * (N + 1)
    
    pq = [(0, X, 0)]
    best_time[X][0] = 0
    
    while pq:
        t, u, c = heapq.heappop(pq)
        
        if c >= min_cost[u]:
            continue
            
        min_cost[u] = c
        
        if u == Y:
            print(t)
            return
            
        for v, dt, dc in adj[u]:
            nxt_t = t + dt
            nxt_c = c + dc
            
            if nxt_c <= V and nxt_t < best_time[v][nxt_c]:
                best_time[v][nxt_c] = nxt_t
                heapq.heappush(pq, (nxt_t, v, nxt_c))
                
    print("-1")

if __name__ == '__main__':
    solve()
