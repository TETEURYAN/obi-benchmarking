import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    E = int(input_data[1])
    S = int(input_data[2])
    M = int(input_data[3])
    
    adj = [[] for _ in range(N)]
    idx = 4
    for _ in range(M):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        t = int(input_data[idx+2])
        adj[u].append((v, t))
        idx += 3
        
    dist = [[-1] * 3 for _ in range(N)]
    dist[E][0] = 0
    
    q = deque([(E, 0)])
    
    while q:
        u, r = q.popleft()
        
        if u == S:
            print(dist[u][r])
            return
            
        d = dist[u][r]
        
        for v, t in adj[u]:
            if r == 0:
                if t != 1:
                    continue
            else:
                if t != 0:
                    continue
                    
            nr = (r + 1) % 3
            if dist[v][nr] == -1:
                dist[v][nr] = d + 1
                q.append((v, nr))
                
    print("*")

if __name__ == '__main__':
    solve()