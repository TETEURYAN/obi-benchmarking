import sys
from collections import deque

def solve():
    data = sys.stdin.read().split()
    idx = 0
    test_num = 0
    
    while True:
        C = int(data[idx]); E = int(data[idx+1]); L = int(data[idx+2]); P = int(data[idx+3])
        idx += 4
        
        if C == 0 and E == 0 and L == 0 and P == 0:
            break
        
        test_num += 1
        
        adj = [[] for _ in range(C + 1)]
        for _ in range(E):
            x = int(data[idx]); y = int(data[idx+1])
            idx += 2
            adj[x].append(y)
            adj[y].append(x)
        
        # BFS with distance limit P
        dist = [-1] * (C + 1)
        dist[L] = 0
        queue = deque([L])
        
        while queue:
            u = queue.popleft()
            if dist[u] < P:
                for v in adj[u]:
                    if dist[v] == -1:
                        dist[v] = dist[u] + 1
                        queue.append(v)
        
        reachable = sorted([i for i in range(1, C + 1) if i != L and dist[i] != -1])
        
        print(f"Teste {test_num}")
        print(*reachable)
        print()

solve()