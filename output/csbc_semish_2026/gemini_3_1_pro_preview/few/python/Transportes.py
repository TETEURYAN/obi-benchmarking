import sys
import heapq

def solve():
    sys.setrecursionlimit(200000)
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
        
    adj = [[] for _ in range(N + 2 * M + 1)]
    state_id = {}
    current_id = N
    
    for _ in range(M):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        c = int(input_data[idx+2])
        idx += 3
        
        if (u, c) not in state_id:
            current_id += 1
            state_id[(u, c)] = current_id
            adj[u].append((current_id, P[c]))
            adj[current_id].append((u, 0))
            
        if (v, c) not in state_id:
            current_id += 1
            state_id[(v, c)] = current_id
            adj[v].append((current_id, P[c]))
            adj[current_id].append((v, 0))
            
        id_u = state_id[(u, c)]
        id_v = state_id[(v, c)]
        
        adj[id_u].append((id_v, 0))
        adj[id_v].append((id_u, 0))
        
    A = int(input_data[idx])
    B = int(input_data[idx+1])
    
    dist = [float('inf')] * (current_id + 1)
    dist[A] = 0
    pq = [(0, A)]
    
    while pq:
        d, u = heapq.heappop(pq)
        
        if d > dist[u]:
            continue
            
        if u == B:
            break
            
        for v, weight in adj[u]:
            if dist[v] > d + weight:
                dist[v] = d + weight
                heapq.heappush(pq, (dist[v], v))
                
    if dist[B] == float('inf'):
        print("-1")
    else:
        print(dist[B])

if __name__ == '__main__':
    solve()