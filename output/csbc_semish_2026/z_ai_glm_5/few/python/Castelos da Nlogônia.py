import sys
from collections import deque

sys.setrecursionlimit(200000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    
    try:
        N = int(next(iterator))
        M = int(next(iterator))
    except StopIteration:
        return

    adj = [[] for _ in range(N + 1)]
    
    for _ in range(N - 1):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u].append(v)
        adj[v].append(u)
        
    colors = [0] * (N + 1)
    
    for _ in range(M):
        p = int(next(iterator))
        q = int(next(iterator))
        c = int(next(iterator))
        
        # BFS to find path from p to q
        parent = [-1] * (N + 1)
        queue = deque([p])
        parent[p] = p
        
        while queue:
            u = queue.popleft()
            if u == q:
                break
            for v in adj[u]:
                if parent[v] == -1:
                    parent[v] = u
                    queue.append(v)
        
        # Reconstruct path
        path_nodes = []
        curr = q
        while True:
            path_nodes.append(curr)
            if curr == p:
                break
            curr = parent[curr]
            
        # Paint
        for node in path_nodes:
            colors[node] = c
            
    print(*(colors[1:]))

if __name__ == "__main__":
    solve()