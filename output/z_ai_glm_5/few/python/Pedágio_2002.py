
import sys
from collections import deque

def solve():
    data = sys.stdin.read().split()
    idx = 0
    test_num = 1
    
    while idx < len(data):
        C = int(data[idx])
        E = int(data[idx + 1])
        L = int(data[idx + 2])
        P = int(data[idx + 3])
        idx += 4
        
        if C == 0 and E == 0 and L == 0 and P == 0:
            break
        
        adj = [[] for _ in range(C + 1)]
        for _ in range(E):
            X = int(data[idx])
            Y = int(data[idx + 1])
            idx += 2
            adj[X].append(Y)
            adj[Y].append(X)
        
        dist = [-1] * (C + 1)
        dist[L] = 0
        queue = deque([L])
        
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                if dist[v] == -1:
                    dist[v] = dist[u] + 1
                    queue.append(v)
        
        result = []
        for i in range(1, C + 1):
            if i != L and dist[i] != -1 and dist[i] <= P:
                result.append(i)
        
        print(f"Teste {test_num}")
        print(' '.join(map(str, result)))
        print()
        test_num += 1

solve()
