import sys
input = sys.stdin.readline

def main():
    import sys
    from sys import setrecursionlimit
    
    data = sys.stdin.read().split()
    idx = 0
    N = int(data[idx]); idx+=1
    M = int(data[idx]); idx+=1
    
    edges = set()
    adj = [[] for _ in range(N+1)]
    
    for _ in range(M):
        x = int(data[idx]); idx+=1
        y = int(data[idx]); idx+=1
        adj[x].append(y)
        adj[y].append(x)
        if x > y:
            x, y = y, x
        edges.add((x, y))
    
    # Find connected components using iterative BFS/DFS
    comp = [-1] * (N+1)
    comp_id = 0
    
    for start in range(1, N+1):
        if comp[start] == -1:
            # BFS
            queue = [start]
            comp[start] = comp_id
            head = 0
            while head < len(queue):
                node = queue[head]; head+=1
                for nb in adj[node]:
                    if comp[nb] == -1:
                        comp[nb] = comp_id
                        queue.append(nb)
            comp_id += 1
    
    # Count sizes of each component
    comp_size = [0] * comp_id
    for i in range(1, N+1):
        comp_size[comp[i]] += 1
    
    # The connectivity value = sum of C(size, 2) for each component
    # Adding edge (A, B) keeps connectivity same if and only if A and B are already in the same component
    # AND there's no existing edge between A and B
    
    # So we need to find two nodes in the same component with no direct edge between them
    # If any component has size >= 3, or size >= 2 and not fully connected (complete graph)
    # A component of size k has at most k*(k-1)/2 edges. If it has fewer, there's a missing edge.
    
    # Strategy: for each component, check if it's a complete graph
    # If not complete, find a missing edge
    
    # Count edges per component
    edge_count = [0] * comp_id
    for (x, y) in edges:
        edge_count[comp[x]] += 1
    
    # Check each component
    for c in range(comp_id):
        sz = comp_size[c]
        max_edges = sz * (sz - 1) // 2
        if edge_count[c] < max_edges:
            # This component is not complete, find a missing edge
            # Collect nodes in this component
            nodes = [i for i in range(1, N+1) if comp[i] == c]
            # Find two nodes with no edge between them
            # Build adjacency set for quick lookup - but could be large
            # Use a smarter approach: for each node, check neighbors
            # We want to find u, v in nodes such that (min(u,v), max(u,v)) not in edges
            
            # Efficient approach: use the "complement graph" idea
            # For small components, brute force
            # For large components, use set difference
            
            # Since total edges <= 400000, if component is large and not complete,
            # we can find missing edge efficiently
            
            # Build neighbor sets for nodes in this component
            # Try each node against all others
            node_set = set(nodes)
            
            found = False
            for u in nodes:
                nb_set = set(adj[u])
                # Find a node in node_set that is not u and not in nb_set
                for v in nodes:
                    if v != u and v not in nb_set:
                        print(u, v)
                        return
                if found:
                    break
            
    print(-1)

main()