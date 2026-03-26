import sys
from collections import deque

def solve():
    data = sys.stdin.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    
    adj = [[] for _ in range(n + 1)]
    radj = [[] for _ in range(n + 1)]
    
    for _ in range(n):
        a = int(data[idx]); idx += 1
        b = int(data[idx]); idx += 1
        adj[a].append(b)
        radj[b].append(a)
    
    # Check strong connectivity using BFS/DFS from node 1 in original graph
    # then BFS/DFS from node 1 in reversed graph
    # If both reach all N nodes, the graph is strongly connected
    
    def bfs(graph, start, n):
        visited = [False] * (n + 1)
        visited[start] = True
        queue = deque([start])
        count = 1
        while queue:
            u = queue.popleft()
            for v in graph[u]:
                if not visited[v]:
                    visited[v] = True
                    count += 1
                    queue.append(v)
        return count
    
    c1 = bfs(adj, 1, n)
    c2 = bfs(radj, 1, n)
    
    if c1 == n and c2 == n:
        print('S')
    else:
        print('N')

solve()