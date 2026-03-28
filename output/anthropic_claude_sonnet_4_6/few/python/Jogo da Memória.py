import sys
from collections import deque

def solve():
    data = sys.stdin.read().split()
    idx = 0
    N = int(data[idx]); idx += 1
    
    C = [0] * (N + 1)
    for i in range(1, N + 1):
        C[i] = int(data[idx]); idx += 1
    
    adj = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        a = int(data[idx]); idx += 1
        b = int(data[idx]); idx += 1
        adj[a].append(b)
        adj[b].append(a)
    
    # For each node, find its pair
    pair = [0] * (N + 1)
    first = {}
    for i in range(1, N + 1):
        c = C[i]
        if c in first:
            pair[i] = first[c]
            pair[first[c]] = i
        else:
            first[c] = i
    
    # We need sum of distances between all pairs
    # Tree has N nodes, N-1 edges
    # For each edge (u,v), when we remove it, it splits tree into two components
    # The contribution of this edge to the total sum is:
    # (number of pairs where one card is in component containing u and other in component containing v)
    
    # Root the tree at node 1, compute subtree sizes
    # For each edge (parent, child), subtree of child has size s
    # Number of pairs crossing = number of pairs with exactly one endpoint in subtree
    
    # For each node i, let's define pair_in_subtree[i] = number of pairs where BOTH endpoints are in subtree of i
    # Actually we need: for edge (p, c), contribution = number of pairs with one in subtree(c) and one outside
    # = (pairs with at least one in subtree(c)) - (pairs with both in subtree(c))
    # But easier: for each pair (u, v), the distance = number of edges on path
    # Each edge contributes 1 to distance of pair (u,v) iff it's on the path
    # Edge (p,c) is on path of pair (u,v) iff exactly one of u,v is in subtree(c)
    
    # So total = sum over edges of (number of pairs crossing that edge)
    # For edge (p,c): let s = subtree size of c
    # pairs_in_subtree = number of pairs with both in subtree(c)
    # pairs_crossing = (N/2) - pairs_in_subtree - pairs_with_neither_in_subtree
    # Actually: pairs_crossing = pairs_with_exactly_one_in_subtree
    # = (pairs with at least one in subtree) - pairs_with_both_in_subtree
    # Let f(c) = number of nodes in subtree(c) whose pair partner is also in subtree(c)
    # Then pairs_with_both = f(c) (each such pair counted once... wait)
    # f(c) = number of complete pairs inside subtree(c)
    # pairs_crossing = f_nodes_in_subtree_with_partner_outside = s - 2*f(c)
    # contribution of edge = s - 2*f(c)  ... wait
    # nodes in subtree = s, complete pairs inside = f(c), so nodes paired inside = 2*f(c)
    # nodes with partner outside = s - 2*f(c)
    # pairs crossing = (s - 2*f(c))  -- each such pair has exactly one node inside
    # So contribution = s - 2*f(c)
    
    # BFS/DFS to compute subtree sizes and f values
    parent = [0] * (N + 1)
    order = []
    visited = [False] * (N + 1)
    stack = [1]
    visited[1] = True
    parent[1] = 0
    while stack:
        u = stack.pop()
        order.append(u)
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                stack.append(v)
    
    subtree_size = [1] * (N + 1)
    complete_pairs = [0] * (N + 1)  # f(c)
    
    # Process in reverse BFS order (leaves first)
    for u in reversed(order):
        p = parent[u]
        if p != 0:
            subtree_size[p] += subtree_size[u]
            complete_pairs[p] += complete_pairs[u]
        # Check if pair[u] is in subtree of u
        # We'll handle this differently
    
    # Need to know for each node if its pair is in its subtree
    # Use euler tour / in-out times
    # Recompute with in/out times
    tin = [0] * (N + 1)
    tout = [0] * (N + 1)
    timer = [0]
    
    stack2 = [(1, False)]
    t = 0
    while stack2:
        u, leaving = stack2.pop()
        if leaving:
            tout[u] = t - 1
        else:
            tin[u] = t
            t += 1
            stack2.append((u, True))
            for v in adj[u]:
                if v != parent[u]:
                    stack2.append((v, False))
    
    def in_subtree(u, v):
        return tin[u] <= tin[v] <= tout[u]
    
    # Recompute complete_pairs
    complete_pairs = [0] * (N + 1)
    subtree_size2 = [1] * (N + 1)
    
    for u in reversed(order):
        p = parent[u]
        if p != 0:
            subtree_size2[p] += subtree_size2[u]
            complete_pairs[p] += complete_pairs[u]
        # if pair[u] is in subtree of u, this pair is complete in subtree of u
        # but we count each pair once: count at LCA
        # Actually count at the node that is ancestor of both
        # Simpler: for each pair (u, pair[u]) with u < pair[u], find if one is in subtree of other
        # Let's just for each node u, check if pair[u] is in subtree of u
        # If yes, complete_pairs[u] += 1 (this pair is fully inside subtree of u)
    
    # Reset and redo
    complete_pairs = [0] * (N + 1)
    for u in range(1, N + 1):
        v = pair[u]
        if in_subtree(u, v):
            complete_pairs[u] += 1
    
    # Now propagate up
    subtree_size = [1] * (N + 1)
    cp = [0] * (N + 1)
    for u in range(1, N + 1):
        cp[u] = complete_pairs[u]
    
    for u in reversed(order):
        p = parent[u]
        if p != 0:
            subtree_size[p] += subtree_size[u]
            cp[p] += cp[u]
    
    total = 0
    for u in order:
        if u == 1:
            continue
        s = subtree_size[u]
        f = cp[u]
        total += s - 2 * f
    
    print(total)

solve()