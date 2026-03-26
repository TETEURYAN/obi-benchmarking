import sys
from collections import defaultdict

def main():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    
    N = int(input_data[idx]); idx += 1
    
    parent = [0] * (N + 1)
    parent[1] = 0
    children = defaultdict(list)
    
    for i in range(2, N + 1):
        p = int(input_data[idx]); idx += 1
        parent[i] = p
        children[p].append(i)
    
    Q = int(input_data[idx]); idx += 1
    
    output = []
    
    for _ in range(Q):
        op = int(input_data[idx]); idx += 1
        v = int(input_data[idx]); idx += 1
        
        if op == 1:
            k = int(input_data[idx]); idx += 1
            cur = v
            for _ in range(k):
                cur = parent[cur]
            output.append(cur)
        else:
            # Restructure from v: all descendants of v become direct children of v
            # BFS/DFS to find all descendants
            # We need to flatten the subtree rooted at v
            stack = list(children[v])
            new_children = []
            while stack:
                node = stack.pop()
                # Add node's children to stack
                for c in children[node]:
                    stack.append(c)
                # node becomes direct child of v (if not already)
                if parent[node] != v:
                    parent[node] = v
                new_children.append(node)
            
            # Update children[v] to be all descendants
            # But we need to clear children of intermediate nodes
            # First collect all descendants
            # Reset children for all nodes in subtree except v
            # We already have new_children list
            
            # Clear children of all descendants
            for node in new_children:
                children[node] = []
            
            # Set children[v] to all new_children
            children[v] = new_children
    
    print('\n'.join(map(str, output)))

main()