import sys
import heapq

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    M = int(input_data[1])
    
    adj = [[] for _ in range(N + 2)]
    
    idx = 2
    for _ in range(M):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        w = int(input_data[idx+2])
        idx += 3
        adj[u].append((v, w))
        adj[v].append((u, w))
        
    dist = [float('inf')] * (N + 2)
    dist[0] = 0
    
    pq = [(0, 0)]
    
    while pq:
        d, u = heapq.heappop(pq)
        
        if d > dist[u]:
            continue
            
        if u == N + 1:
            print(d)
            return
            
        for v, w in adj[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))

if __name__ == '__main__':
    main()