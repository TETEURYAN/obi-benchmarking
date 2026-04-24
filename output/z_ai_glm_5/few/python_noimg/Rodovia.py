import sys

# Increase recursion depth for Kosaraju's algorithm on large graphs
sys.setrecursionlimit(300000)

def solve():
    # Use fast I/O
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    try:
        N = int(next(iterator))
        M = int(next(iterator))
    except StopIteration:
        return

    adj = [[] for _ in range(N)]
    rev_adj = [[] for _ in range(N)]
    edges = set()

    for _ in range(M):
        u = int(next(iterator)) - 1
        v = int(next(iterator)) - 1
        adj[u].append(v)
        rev_adj[v].append(u)
        edges.add((u, v))

    # Kosaraju's algorithm to find Strongly Connected Components
    visited = [False] * N
    order = []

    def dfs1(u):
        visited[u] = True
        for v in adj[u]:
            if not visited[v]:
                dfs1(v)
        order.append(u)

    for i in range(N):
        if not visited[i]:
            dfs1(i)

    visited = [False] * N
    sccs = []
    
    def dfs2(u, component):
        visited[u] = True
        component.append(u)
        for v in rev_adj[u]:
            if not visited[v]:
                dfs2(v, component)

    for u in reversed(order):
        if not visited[u]:
            component = []
            dfs2(u, component)
            sccs.append(component)

    # Check SCCs with size > 1
    # If an SCC has size K > 1, any pair (u, v) within it is reachable.
    # We just need to find a pair that is not already an edge.
    for component in sccs:
        if len(component) > 1:
            # We iterate through pairs in the SCC.
            # If the SCC is a clique, we iterate all K*(K-1) pairs.
            # Since M >= K*(K-1) in that case, total work is bounded by O(M).
            # If not a clique, we stop early.
            for u in component:
                for v in component:
                    if u != v:
                        if (u, v) not in edges:
                            print(f"{u+1} {v+1}")
                            return

    # If no SCC with size > 1, the graph is a DAG.
    # We need to find u -> v -> w such that (u, w) is not an edge.
    # This implies a path of length >= 2 without a shortcut.
    
    limit = int(M**0.5) + 1
    
    # Identify heavy nodes: out-degree > sqrt(M)
    heavy_nodes = set()
    for u in range(N):
        if len(adj[u]) > limit:
            heavy_nodes.add(u)

    # Precompute bitmasks for heavy nodes
    # Using Python integers as bitsets
    heavy_masks = {}
    for u in heavy_nodes:
        mask = 0
        for v in adj[u]:
            mask |= (1 << v)
        heavy_masks[u] = mask

    # Iterate all edges u -> v
    for u in range(N):
        # mask_u is computed lazily
        mask_u = -1 
        
        for v in adj[u]:
            if v not in heavy_nodes:
                # v is light: iterate all w such that v -> w
                # Cost: sum of (in-deg(v) * out-deg(v)) for light v
                # Bounded by O(M * sqrt(M))
                for w in adj[v]:
                    if (u, w) not in edges:
                        print(f"{u+1} {w+1}")
                        return
            else:
                # v is heavy
                if mask_u == -1:
                    # Compute mask for u
                    m = 0
                    for x in adj[u]:
                        m |= (1 << x)
                    mask_u = m
                
                mask_v = heavy_masks[v]
                
                # Check if adj[v] is a subset of adj[u]
                # If (mask_v & ~mask_u) != 0, there exists w in adj[v] not in adj[u]
                if (mask_v & (~mask_u)) != 0:
                    # Find such a w
                    # Since we know it exists, this loop is efficient enough (or we iterate adj[v])
                    for w in adj[v]:
                        if (u, w) not in edges:
                            print(f"{u+1} {w+1}")
                            return

    print("-1")

if __name__ == '__main__':
    solve()