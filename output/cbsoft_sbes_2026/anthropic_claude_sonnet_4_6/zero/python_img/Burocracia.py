
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
    
    # For restructuring: when we restructure from v,
    # all nodes that have v as ancestor become direct children of v.
    # This is essentially path compression in a union-find like structure,
    # but we need to maintain the ability to go k levels up.
    
    # We'll use a "level" approach with binary lifting, but restructuring
    # changes the tree dynamically.
    
    # Since N <= 1e5 and Q <= 5e4, we can afford O(N) per restructuring
    # and O(depth) per query if depth is small after restructuring.
    
    # After restructuring from v, all descendants of v are at depth 1 from v.
    # So the tree becomes flat under v.
    
    # Key insight: restructuring from v makes all descendants direct children of v.
    # So after restructuring, any node u that was a descendant of v now has parent[u] = v.
    
    # For query (1, v, k): walk up k levels from v.
    # For restructuring (2, v): for all descendants of v (not v itself), set parent to v.
    
    # The challenge: efficiently finding all descendants of v for restructuring.
    # And efficiently walking up k levels for queries.
    
    # Since after restructuring from v, all descendants are at depth 1,
    # subsequent restructurings from v's ancestors will be fast.
    
    # Let's maintain children lists and do BFS for restructuring.
    
    children = [[] for _ in range(N + 1)]
    for i in range(2, N + 1):
        children[parent[i]].append(i)
    
    output = []
    
    for _ in range(Q):
        op = int(data[idx]); idx += 1
        v = int(data[idx]); idx += 1
        
        if op == 1:
            k = int(data[idx]); idx += 1
            # Walk k levels up from v
            cur = v
            for _ in range(k):
                cur = parent[cur]
            output.append(cur)
        else:
            # Restructure from v: all descendants become direct children of v
            # BFS/DFS to find all descendants
            # We need to flatten: for each child c of v, if c has children,
            # we need to move all descendants of c to be children of v
            
            # Collect all descendants (not v itself)
            # Then set their parent to v and update children list
            
            # We do BFS starting from children of v
            # For each node at depth >= 2 from v, move to depth 1
            
            # First, collect all nodes at depth >= 2 from v
            new_children_of_v = []
            
            # BFS
            queue = []
            # Start with children of v's children (depth 2+)
            for c in children[v]:
                for gc in children[c]:
                    queue.append(gc)
            
            # Process queue: these are all at depth >= 2 from v
            # We need to collect ALL descendants at depth >= 2
            i2 = 0
            while i2 < len(queue):
                node = queue[i2]; i2 += 1
                new_children_of_v.append(node)
                for ch in children[node]:
                    queue.append(ch)
                children[node] = []
                parent[node] = v
            
            # Add them to children[v]
            children[v].extend(new_children_of_v)
    
    print('\n'.join(map(str, output)))

main()
