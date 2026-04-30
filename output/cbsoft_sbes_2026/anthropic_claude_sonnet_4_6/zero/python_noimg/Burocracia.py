import sys
from sys import stdin

def main():
    input = stdin.readline
    data = sys.stdin.read().split()
    idx = 0
    
    N = int(data[idx]); idx += 1
    
    parent = [0] * (N + 1)
    parent[1] = 0  # king has no parent
    
    for i in range(2, N + 1):
        parent[i] = int(data[idx]); idx += 1
    
    Q = int(data[idx]); idx += 1
    
    # For restructuring from v: all nodes that have v as ancestor become direct children of v
    # This is essentially path compression in a tree
    # 
    # We need to support:
    # 1. Query: given node v and k, find ancestor k levels above v
    # 2. Update: restructure from v (flatten all descendants to be direct children of v)
    #
    # Key insight: after restructuring from v, all descendants of v are at depth 1 from v
    # So when we query k levels above u, we need to traverse the current parent structure
    #
    # Since restructuring flattens subtrees, the depth of any node can only decrease over time
    # 
    # For query type 1: we need to go k levels up from v
    # After restructuring operations, many nodes will have their parent set to v directly
    #
    # Naive approach: for each query, walk up k steps. For restructure, BFS/DFS and update parents.
    # With N=1e5 and Q=5e4, naive might be too slow but let's think about bounds.
    #
    # After restructuring from v, all descendants become depth 1 from v.
    # So the tree height can only decrease. Total restructuring work is O(N) amortized across all ops.
    # For queries, each step costs O(1), but k can be up to N.
    # However, after restructurings, depths are small.
    #
    # Let's implement restructure with BFS (collect all descendants, set parent to v)
    # and query by walking up.
    # 
    # Build children list for efficient restructuring
    
    children = [[] for _ in range(N + 1)]
    for i in range(2, N + 1):
        children[parent[i]].append(i)
    
    # Restructure from v: all nodes in subtree of v (except v itself) become direct children of v
    def restructure(v):
        # BFS to find all descendants
        # We need to flatten: all nodes at depth >= 2 from v become direct children of v
        # First collect all nodes at depth >= 2
        new_children = []
        # BFS level by level
        queue = list(children[v])
        # children at depth 1 stay, but their children (depth 2+) need to move
        # Actually we need to go deeper
        # Let's do full BFS of subtree of v, collect all nodes except direct children
        # Then set their parent to v and update children list
        
        # Collect all descendants
        stack = list(children[v])
        all_desc = []
        while stack:
            node = stack.pop()
            all_desc.append(node)
            stack.extend(children[node])
        
        # Now set all descendants as direct children of v
        # Clear children of v first, then add all descendants
        # Also clear children of all descendants (since they're now direct children of v)
        
        # Reset children for all descendants
        for node in all_desc:
            children[node] = []
            parent[node] = v
        
        children[v] = all_desc
    
    output = []
    
    for _ in range(Q):
        op = int(data[idx]); idx += 1
        v = int(data[idx]); idx += 1
        
        if op == 2:
            restructure(v)
        else:
            k = int(data[idx]); idx += 1
            # Find ancestor k levels above v
            cur = v
            for _ in range(k):
                cur = parent[cur]
            output.append(cur)
    
    print('\n'.join(map(str, output)))

main()