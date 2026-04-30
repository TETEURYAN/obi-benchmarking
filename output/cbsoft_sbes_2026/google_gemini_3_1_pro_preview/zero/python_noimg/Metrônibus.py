
import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    K1 = int(input_data[1])
    K2 = int(input_data[2])
    P = int(input_data[3])
    
    adj = [[] for _ in range(2 * N + 1)]
    
    idx = 4
    for _ in range(K1):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        idx += 2
        adj[u].append((v, 0))
        adj[v].append((u, 0))
        
    for _ in range(K2):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        idx += 2
        adj[u + N].append((v + N, 0))
        adj[v + N].append((u + N, 0))
        
    A = int(input_data[idx])
    B = int(input_data[idx+1])
    
    for i in range(1, N + 1):
        adj[i].append((i + N, 1))
        adj[i + N].append((i, 1))
        
    INF = 10**9
    dist = [INF] * (2 * N + 1)
    dist[A] = 1
    dist[A + N] = 1
    
    q = deque([(A, 1), (A + N, 1)])
    
    while q:
        u, d_u = q.popleft()
        
        if d_u > dist[u]:
            continue
            
        for v, w in adj[u]:
            if dist[v] > d_u + w:
                dist[v] = d_u + w
                if w == 0:
                    q.appendleft((v, dist[v]))
                else:
                    q.append((v, dist[v]))
                    
    ans = min(dist[B], dist[B + N])
    if ans == INF:
        print("-1")
    else:
        print(ans * P)

if __name__ == '__main__':
    solve()
