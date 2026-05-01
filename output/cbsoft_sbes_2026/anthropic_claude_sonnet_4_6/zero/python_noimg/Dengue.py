import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    idx = 0
    test_num = 0
    
    while idx < len(input_data):
        N = int(input_data[idx]); idx += 1
        
        if N == 0:
            break
        
        test_num += 1
        
        if N == 1:
            # Read 0 edges
            print(f"Teste {test_num}")
            print(1)
            print()
            continue
        
        adj = [[] for _ in range(N + 1)]
        for _ in range(N - 1):
            x = int(input_data[idx]); idx += 1
            y = int(input_data[idx]); idx += 1
            adj[x].append(y)
            adj[y].append(x)
        
        # Find the center of the tree (minimizes eccentricity = max distance)
        # Algorithm: repeatedly remove leaves until 1 or 2 nodes remain
        # Those are the centers
        
        # BFS from each node to find eccentricity - O(N^2) which is fine for N<=100
        def bfs_max_dist(start):
            dist = [-1] * (N + 1)
            dist[start] = 0
            q = deque([start])
            max_d = 0
            while q:
                u = q.popleft()
                for v in adj[u]:
                    if dist[v] == -1:
                        dist[v] = dist[u] + 1
                        if dist[v] > max_d:
                            max_d = dist[v]
                        q.append(v)
            return max_d
        
        best_node = 1
        best_ecc = float('inf')
        
        for node in range(1, N + 1):
            ecc = bfs_max_dist(node)
            if ecc < best_ecc:
                best_ecc = ecc
                best_node = node
        
        print(f"Teste {test_num}")
        print(best_node)
        print()

solve()