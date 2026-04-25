import sys
from collections import deque

def solve():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(input_data[idx]); idx += 1
    
    adj = [[] for _ in range(n + 1)]
    degree = [0] * (n + 1)
    
    for _ in range(n - 1):
        u = int(input_data[idx]); idx += 1
        v = int(input_data[idx]); idx += 1
        adj[u].append(v)
        adj[v].append(u)
        degree[u] += 1
        degree[v] += 1
    
    # Capitals are leaves (degree == 1)
    # Non-capitals have degree >= 2
    # We need minimum distance between any pair of capitals
    
    # The path between two capitals goes through internal nodes
    # We need to find the minimum distance between any two leaves
    
    # Key insight: The minimum distance between two leaves is achieved by
    # two leaves that share a common neighbor (internal node), giving distance 2,
    # OR two leaves connected directly (distance 1, only possible if n=2).
    
    # Wait, if n=2, both nodes have degree 1, so both are capitals, distance=1.
    
    # For n>2: can two capitals be adjacent? If u-v is an edge and both have degree 1,
    # that means n=2. For n>2, if u is a leaf and v is a leaf connected to each other,
    # then they have degree 1 but the tree would need to have other nodes connected elsewhere.
    # Actually if u-v edge exists and degree[u]=1 and degree[v]=1, then n=2.
    
    # So for n>2, minimum distance between two leaves:
    # - If an internal node has >= 2 leaf neighbors, answer is 2
    # - Otherwise, we need BFS/tree DP to find minimum distance between leaves
    
    # Check if any internal node has 2+ leaf children -> answer = 2
    leaf_neighbor_count = [0] * (n + 1)
    for v in range(1, n + 1):
        if degree[v] == 1:
            # v is a leaf, its single neighbor
            u = adj[v][0]
            leaf_neighbor_count[u] += 1
    
    for v in range(1, n + 1):
        if leaf_neighbor_count[v] >= 2:
            print(2)
            return
    
    if n == 2:
        print(1)
        return
    
    # No internal node has 2+ leaf neighbors
    # Each internal node has at most 1 leaf neighbor
    # We need minimum distance between two leaves
    # This is a tree problem: find min distance between any two leaves
    
    # Build a compressed tree or do BFS from each leaf? Too slow for n=1e5
    
    # Better approach: For each internal node, track the two closest leaves
    # Use tree DP
    
    # dp[v] = minimum distance from v to a leaf in its subtree (rooted tree)
    # For each node, combine distances from different subtrees
    
    INF = float('inf')
    
    # Root at node with degree >= 2 (any internal node)
    root = -1
    for v in range(1, n + 1):
        if degree[v] >= 2:
            root = v
            break
    
    # Iterative DFS
    parent = [-1] * (n + 1)
    order = []
    visited = [False] * (n + 1)
    stack = [root]
    visited[root] = True
    while stack:
        v = stack.pop()
        order.append(v)
        for u in adj[v]:
            if not visited[u]:
                visited[u] = True
                parent[u] = v
                stack.append(u)
    
    # dp[v] = min distance from v to any leaf in subtree of v
    dp = [INF] * (n + 1)
    
    # Leaves have dp = 0
    for v in range(1, n + 1):
        if degree[v] == 1:
            dp[v] = 0
    
    ans = INF
    
    # Process in reverse order (bottom-up)
    for v in reversed(order):
        # Collect dp values from children
        # For combining: find two smallest dp values from different children
        best1 = INF
        best2 = INF
        
        if degree[v] == 1:
            dp[v] = 0
            continue
        
        for u in adj[v]:
            if u == parent[v]:
                continue
            val = dp[u] + 1
            if val < best1:
                best2 = best1
                best1 = val
            elif val < best2:
                best2 = val
        
        # Also consider parent direction later, but for now:
        if best1 != INF and best2 != INF:
            ans = min(ans, best1 + best2)
        
        dp[v] = best1 if best1 != INF else INF
    
    # Now we need to also consider paths that go through parent
    # Re-root DP: for each node v, also know best distance to leaf going "up"
    
    up = [INF] * (n + 1)
    # up[root] = INF (no parent)
    
    for v in order:
        # Compute up values for children of v
        children_vals = []
        for u in adj[v]:
            if u == parent[v]:
                continue
            children_vals.append((dp[u] + 1, u))
        
        # Also include up[v]+1 as a direction
        all_vals = children_vals[:]
        if up[v] != INF:
            all_vals.append((up[v] + 1, -1))
        
        all_vals.sort()
        
        for u in adj[v]:
            if u == parent[v]:
                continue
            # up[u] = min distance to leaf not going through u
            # = min of (dp[other_child]+1 for other children) and (up[v]+1)
            child_val = dp[u] + 1
            # find best among all_vals excluding u
            best = INF
            for val, node in all_vals:
                if node != u:
                    best = val
                    break
            up[u] = best
            
            # Update answer: path from leaf in u's subtree to leaf via up
            if dp[u] != INF and up[u] != INF:
                ans = min(ans, dp[u] + 1 + up[u])
    
    print(ans)

solve()