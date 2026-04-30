import sys
from collections import deque

def solve():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    N = int(input_data[idx]); idx += 1
    
    adj = [[] for _ in range(N + 1)]
    degree = [0] * (N + 1)
    
    for _ in range(N - 1):
        u = int(input_data[idx]); idx += 1
        v = int(input_data[idx]); idx += 1
        adj[u].append(v)
        adj[v].append(u)
        degree[u] += 1
        degree[v] += 1
    
    # Capitals are nodes with degree 1
    # Non-capitals have degree >= 2
    # We need minimum distance between any pair of capitals
    
    # The tree structure: capitals are leaves
    # We need to find the minimum distance between any two leaves
    
    # Key insight: the minimum distance between two leaves is achieved by
    # two leaves that share a common non-leaf neighbor, or are directly connected
    # (but if N=2, both are leaves connected directly)
    
    # Actually, for any internal node (non-capital), we can find the two closest
    # leaves in its subtrees. The minimum path through an internal node between
    # two leaves is the sum of distances to the two closest leaves in different subtrees.
    
    # Better approach: For each internal node, find the distances to leaves in each
    # of its subtree branches. The minimum pair uses the two smallest distances
    # from different branches.
    
    # We can do this with a single DFS/BFS approach.
    # For each node, compute the minimum distance to a leaf in each adjacent subtree.
    
    # Use iterative post-order DFS
    # For each node, store the minimum leaf distance from each child subtree
    # Then for each node, the best pair through it = min1 + min2 + 2 (if internal)
    # where min1, min2 are the two smallest distances from different children
    
    # If node is internal (degree >= 2), distance to leaf in a subtree rooted at child c
    # is 1 + min_leaf_dist[c] (where min_leaf_dist[c] is min dist from c to a leaf in c's subtree)
    
    # If node is a leaf, min_leaf_dist = 0
    
    INF = float('inf')
    
    if N == 2:
        print(1)
        return
    
    # Root the tree at node with degree >= 2
    root = -1
    for i in range(1, N + 1):
        if degree[i] >= 2:
            root = i
            break
    
    # Iterative DFS
    parent = [0] * (N + 1)
    order = []
    visited = [False] * (N + 1)
    stack = [root]
    visited[root] = True
    parent[root] = -1
    
    while stack:
        node = stack.pop()
        order.append(node)
        for nb in adj[node]:
            if not visited[nb]:
                visited[nb] = True
                parent[nb] = node
                stack.append(nb)
    
    # min_dist[node] = minimum distance from node to any leaf in its subtree
    min_dist = [INF] * (N + 1)
    
    # For leaves (degree 1), min_dist = 0
    for i in range(1, N + 1):
        if degree[i] == 1:
            min_dist[i] = 0
    
    ans = INF
    
    # Process in reverse order (post-order)
    for node in reversed(order):
        if degree[node] == 1:
            min_dist[node] = 0
            continue
        
        # Collect min distances from children subtrees
        # distance from node to leaf through child c = 1 + min_dist[c]
        child_dists = []
        for nb in adj[node]:
            if nb == parent[node]:
                continue
            if min_dist[nb] < INF:
                child_dists.append(1 + min_dist[nb])
        
        if len(child_dists) == 0:
            continue
        
        child_dists.sort()
        
        # Update min_dist for this node
        min_dist[node] = child_dists[0]
        
        # If we have at least 2 children with leaf paths, we can form a pair
        if len(child_dists) >= 2:
            candidate = child_dists[0] + child_dists[1]
            if candidate < ans:
                ans = candidate
        
        # Also consider path from parent side: but we handle that when processing parent
    
    # Also need to consider paths that go through the root from different sides
    # Already handled above since root is processed too
    
    # Edge case: if a capital is directly connected to another capital (N=2 handled)
    # Check if any two leaves are directly connected (shouldn't happen given constraints
    # since non-capitals have degree >= 2, but just in case)
    
    print(ans)

solve()