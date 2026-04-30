import sys
from sys import setrecursionlimit

def main():
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
    
    # Iterative DFS to compute size and check balance
    # Returns (size, is_balanced)
    
    balanced = True
    size = [0] * (N + 1)
    
    # Topological order using iterative post-order DFS
    stack = [root]
    order = []
    visited = [False] * (N + 1)
    
    while stack:
        node = stack.pop()
        if visited[node]:
            continue
        visited[node] = True
        order.append(node)
        for child in children[node]:
            stack.append(child)
    
    # Process in reverse order (post-order)
    for node in reversed(order):
        size[node] = 1
        for child in children[node]:
            size[node] += size[child]
        
        # Check balance: all children must have same size
        if children[node]:
            first_size = size[children[node][0]]
            for child in children[node]:
                if size[child] != first_size:
                    balanced = False
                    break
    
    print("bem" if balanced else "mal")

main()