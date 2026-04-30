import sys
from sys import setrecursionlimit

def solve():
    input_data = sys.stdin.read().split()
    idx = 0
    N = int(input_data[idx]); idx += 1
    
    children = [[] for _ in range(N + 1)]
    root = -1
    
    for _ in range(N):
        I = int(input_data[idx]); idx += 1
        J = int(input_data[idx]); idx += 1
        if J == 0:
            root = I
        else:
            children[J].append(I)
    
    setrecursionlimit(20000)
    
    balanced = True
    
    # Iterative DFS to compute subtree sizes and check balance
    # Returns size of subtree rooted at node, or -1 if unbalanced
    
    # Use iterative post-order traversal
    stack = [(root, False)]
    size = [0] * (N + 1)
    
    while stack:
        node, processed = stack.pop()
        if processed:
            # Compute size and check balance
            if not children[node]:
                size[node] = 1
            else:
                child_sizes = [size[c] for c in children[node]]
                if len(set(child_sizes)) > 1:
                    balanced = False
                size[node] = 1 + sum(child_sizes)
        else:
            stack.append((node, True))
            for c in children[node]:
                stack.append((c, False))
    
    print("bem" if balanced else "mal")

solve()