
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
        
    adj = [[] for _ in range(N + 1)]
    id_map = {}
    curr_id = N
    
    for _ in range(M):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        c = int(input_data[idx+2])
        idx += 3
        
        uid = id_map.get((u, c))
        if uid is None:
            curr_id += 1
            uid = curr_id
            id_map[(u, c)] = uid
            adj.append([])
            adj[u].append((uid, P[c]))
            adj[uid].append((u, 0))
            
        vid = id_map.get((v, c))
        if vid is None:
            curr_id += 1
            vid = curr_id
            id_map[(v, c)] = vid
            adj.append([])
            adj[v].append((vid, P[c]))
            adj[vid].append((v, 0))
            
        adj[uid].append((vid, 0))
        adj[vid].append((uid, 0))
        
    A = int(input_data[idx])
    B = int(input_data[idx+1])
    
    dist = [10**15] * (curr_id + 1)
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
            if d + w < dist[v]:
                dist[v] = d + w
                heappush(pq, (dist[v], v))
                
    print(-1)

if __name__ == '__main__':
    solve()
