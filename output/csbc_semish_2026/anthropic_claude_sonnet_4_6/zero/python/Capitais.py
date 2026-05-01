Looking at this problem:

- We have a tree of N cities
- **Capitals** are nodes with degree 1 (leaves) - they connect to exactly one other city
- **Non-capitals** have degree ≥ 2
- No path between two capitals passes through another capital (this is guaranteed by the tree structure with leaves)
- Find the minimum distance between any pair of capitals (leaves)

So I need to find the minimum distance between any two leaf nodes in a tree.

**Approach:**
- For each leaf, the path to another leaf goes through their LCA
- The minimum distance between two leaves is at least 2 (if they share the same parent non-leaf)
- I need to find the minimum distance between any two leaves

**Key insight:** The minimum distance between two leaves will be found by looking at each internal node and finding the two closest leaves in different subtrees.

For each non-leaf node, I can compute the distance to the nearest leaf in each of its subtrees, then combine the two smallest distances from different children.

**Algorithm:**
1. For each node, compute `min_leaf_dist[v]` = minimum distance from v to any leaf in its subtree
2. For leaves: `min_leaf_dist[leaf] = 0`
3. For internal nodes: `min_leaf_dist[v] = 1 + min(min_leaf_dist[child] for child in children)`
4. For each internal node, the answer candidate is: sum of two smallest `(1 + min_leaf_dist[child])` values across children

This gives O(N) solution.

```python
import sys
from collections import defaultdict
input = sys.stdin.readline

def solve():
    sys.setrecursionlimit(200000)
    N = int(input())
    adj = defaultdict(list)
    degree = [0] * (N + 1)
    
    for _ in range(N - 1):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
        degree[u] += 1
        degree[v] += 1
    
    if N == 2:
        print(1)
        return
    
    # min_leaf_dist[v] = min distance from v to a leaf in its subtree
    min_leaf_dist = [float('inf')] * (N + 1)
    
    ans = float('inf')
    
    # Iterative DFS (post-order)
    root = 1
    # Find a non-leaf root
    for i in range(1, N + 1):
        if degree[i] > 1:
            root = i
            break
    
    parent = [-1] * (N + 1)
    order = []
    visited = [False] * (N + 1)
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
    
    # Process in reverse order (post-order)
    for v in reversed(order):
        if degree[v] == 1:
            # It's a leaf (capital)
            min_leaf_dist[v] = 0
        else:
            # Internal node: find two smallest (1 + min_leaf_dist[child]) among children
            children_dists = []
            for u in adj[v]:
                if u != parent[v]:
                    if min_leaf_dist[u] != float('inf'):
                        children_dists.append(1 + min_leaf_dist[u])
            
            # Also consider parent direction? No - we process subtree first
            # min_leaf_dist[v] = min of children_dists
            if children_dists:
                children_dists.sort()
                min_leaf_dist[v] = children_dists[0]
                if len(children_dists) >= 2:
                    candidate = children_dists[0] + children_dists[1]
                    ans = min(ans, candidate)
    
    # Also need to consider paths going through parent
    # Re-process with full distances (both up and down)
    # Actually the above misses paths that go up then down
    # Need to do rerooting DP
    
    # min_dist_full[v] = min distance from v to any leaf (entire tree)
    min_dist_full = list(min_leaf_dist)
    
    for v in order:
        # Update children with distance through parent
        p = parent[v]
        if p != -1:
            val = min_dist_full[p] + 1
            if val < min_dist_full[v]:
                min_dist_full[v] = val
        # Now update answer for internal nodes using full distances
    
    # Recompute answer with full distances
    ans2 = float('inf')
    for v in order:
        if degree[v] > 1:
            dists = []
            for u in adj[v]:
                dists.append(1 + min_dist_full[u])
            dists.sort()
            if len(dists) >= 2:
                ans2 = min(ans2, dists[0] + dists[1])
    
    print(min(ans, ans2))

solve()
```