import sys
from heapq import heappush, heappop

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
    
    min_time = [[float('inf')] * (V + 1) for _ in range(N + 1)]
    for k in range(V + 1):
        min_time[X][k] = 0
        
    pq = [(0, X, 0)]
    
    while pq:
        t, u, c = heappop(pq)
        
        if t > min_time[u][c]:
            continue
            
        if u == Y:
            print(t)
            return
            
        for v, dt, dp in adj[u]:
            nc = c + dp
            if nc <= V:
                nt = t + dt
                if nt < min_time[v][nc]:
                    for k in range(nc, V + 1):
                        if min_time[v][k] <= nt:
                            break
                        min_time[v][k] = nt
                    heappush(pq, (nt, v, nc))
                    
    print(-1)

if __name__ == '__main__':
    solve()