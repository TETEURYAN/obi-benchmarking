import sys
from heapq import heappush, heappop

def solve():
    input_data = sys.stdin.read().split()
    idx = 0
    N = int(input_data[idx]); idx += 1
    M = int(input_data[idx]); idx += 1
    
    adj = [[] for _ in range(N)]
    edges = []
    
    for _ in range(M):
        p = int(input_data[idx]); idx += 1
        q = int(input_data[idx]); idx += 1
        u = int(input_data[idx]); idx += 1
        adj[p].append((u, q))
        adj[q].append((u, p))
        edges.append((u, p, q))
    
    # The problem asks for minimum cost spanning tree rooted at some node,
    # where all nodes travel to the root.
    # Since bus cost is fixed regardless of passengers, we need a minimum spanning tree
    # and the cost is the sum of edges in the MST.
    # The meeting colony can be any colony, but since the graph is connected and
    # we want all nodes to reach one colony, we need a spanning tree.
    # The minimum cost is the MST cost (sum of edges used).
    # The root doesn't matter for MST cost.
    
    # Kruskal's algorithm for MST
    edges.sort()
    
    parent = list(range(N))
    rank = [0] * N
    
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    
    def union(x, y):
        rx, ry = find(x), find(y)
        if rx == ry:
            return False
        if rank[rx] < rank[ry]:
            rx, ry = ry, rx
        parent[ry] = rx
        if rank[rx] == rank[ry]:
            rank[rx] += 1
        return True
    
    total = 0
    count = 0
    for u, p, q in edges:
        if union(p, q):
            total += u
            count += 1
            if count == N - 1:
                break
    
    print(total)

solve()