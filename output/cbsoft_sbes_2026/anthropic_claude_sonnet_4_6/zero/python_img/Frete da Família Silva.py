import heapq
import sys
input = sys.stdin.readline

def dijkstra(graph, start, n):
    dist = [float('inf')] * n
    dist[start] = 0
    pq = [(0, start)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))
    return dist

def main():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]
    for _ in range(m):
        p, q, u = map(int, input().split())
        graph[p].append((q, u))
        graph[q].append((p, u))
    
    # For each colony as meeting point, compute sum of shortest paths from all others
    # We need minimum spanning tree approach or all-pairs shortest paths
    # Since we want to find the colony that minimizes total cost to bring everyone there
    # The cost is: for each colony i != root, shortest path from i to root
    # But people can share rides (buses carry infinite people at fixed cost)
    # So the cost is the minimum spanning tree rooted at the meeting point
    # Actually, the cost is the MST of the graph (since edges can be shared)
    # Wait - let's think again:
    # The cost is the sum of edges in a Steiner tree connecting all nodes to root
    # Since the graph is undirected and we want all nodes to reach root,
    # the optimal is to use a minimum spanning tree (MST) - the total cost equals MST weight
    # regardless of which node is the root!
    # Because in MST, every edge is used exactly once to connect components,
    # and the total cost is fixed regardless of root.
    
    # Let's verify with example 1:
    # Edges: 0-1:10, 0-2:5, 0-3:10, 1-2:3, 1-3:4, 2-3:2
    # MST: 2-3:2, 1-2:3, 1-3:4 -> but that's a cycle... 
    # MST: 2-3:2, 1-2:3, 0-2:5 -> total = 10. Yes! matches output.
    
    # Example 2: 0-1:1, 0-2:1, 0-3:1, 1-2:3, 1-3:4, 2-3:2
    # MST: 0-1:1, 0-2:1, 0-3:1 -> total = 3. Yes! matches output.
    
    # So the answer is just the MST weight!
    
    # Kruskal's algorithm
    edges = []
    for u in range(n):
        for v, w in graph[u]:
            if u < v:
                edges.append((w, u, v))
    edges.sort()
    
    parent = list(range(n))
    rank = [0] * n
    
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
    for w, u, v in edges:
        if union(u, v):
            total += w
            count += 1
            if count == n - 1:
                break
    
    print(total)

main()