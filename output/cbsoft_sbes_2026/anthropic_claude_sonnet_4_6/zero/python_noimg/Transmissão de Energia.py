import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    idx = 0
    test_num = 1
    
    while idx < len(input_data):
        E = int(input_data[idx]); L = int(input_data[idx+1])
        idx += 2
        
        if E == 0 and L == 0:
            break
        
        adj = [[] for _ in range(E + 1)]
        
        for _ in range(L):
            x = int(input_data[idx]); y = int(input_data[idx+1])
            idx += 2
            adj[x].append(y)
            adj[y].append(x)
        
        # BFS from node 1
        visited = [False] * (E + 1)
        queue = deque([1])
        visited[1] = True
        count = 1
        
        while queue:
            node = queue.popleft()
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    count += 1
                    queue.append(neighbor)
        
        print(f"Teste {test_num}")
        if count == E:
            print("normal")
        else:
            print("falha")
        print()
        
        test_num += 1

solve()