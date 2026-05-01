
import sys
from heapq import heappush, heappop

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    M = int(input_data[1])
    K = int(input_data[2])
    
    P = [0] * (K + 1)
    idx = 3
    for i in range(1, K + 1):
        P[i] = int(input_data[idx])
        idx += 1
        
    state_id = {}
    id_counter = N + 1
    
    edges = []
    for _ in range(M):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        c = int(input_data[idx+2])
        idx += 3
        edges.append((u, v, c))
        
    A = int(input_data[idx])
    B = int(input_data[idx+1])
    
    for u, v, c in edges:
        key_u = u * 100005 + c
        if key_u not in state_id:
            state_id[key_u] = id_counter
            id_counter += 1
        key_v = v * 100005 + c
        if key_v not in state_id:
            state_id[key_v] = id_counter
            id_counter += 1
            
    adj = [[] for _ in range(id_counter)]
    
    for key, sid in state_id.items():
        u = key // 100005
        c = key % 100005
        adj[u].append((sid, P[c]))
        adj[sid].append((u, 0))
        
    for u, v, c in edges:
        su = state_id[u * 100005 + c]
        sv = state_id[v * 100005 + c]
        adj[su].append((sv, 0))
        adj[sv].append((su, 0))
        
    dist = [float('inf')] * id_counter
    dist[A] = 0
    pq = [(0, A)]
    
    while pq:
        d, u = heappop(pq)
        
        if d > dist[u]:
            continue
            
        if u == B:
            print(d)
            return
            
        for v, w in adj[u]:
            if dist[v] > d + w:
                dist[v] = d + w
                heappush(pq, (dist[v], v))
                
    print(-1)

if __name__ == '__main__':
    solve()
