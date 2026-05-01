
import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    ptr = 0
    N = int(data[ptr])
    ptr += 1
    p = [0] * (N + 1)
    for i in range(2, N + 1):
        p[i] = int(data[ptr])
        ptr += 1
    Q = int(data[ptr])
    ptr += 1

    # Preprocess parent and depth arrays
    parent = [0] * (N + 1)
    depth = [0] * (N + 1)
    for i in range(2, N + 1):
        parent[i] = p[i]
        depth[i] = depth[p[i]] + 1

    # Process operations
    output = []
    for _ in range(Q):
        op = data[ptr]
        ptr += 1
        if op == '1':
            v = int(data[ptr])
            ptr += 1
            k = int(data[ptr])
            ptr += 1
            current = v
            remaining_k = k
            while remaining_k > 0:
                if depth[current] < remaining_k:
                    break
                if remaining_k >= depth[current]:
                    current = parent[current]
                    remaining_k -= 1
                else:
                    break
            output.append(str(current))
        else:
            v = int(data[ptr])
            ptr += 1
            # Perform restructuring: all nodes in subtree of v become direct children of v
            # We need to update parent and depth for all nodes in the subtree
            stack = [v]
            while stack:
                node = stack.pop()
                if node == v:
                    continue
                parent[node] = v
                depth[node] = depth[v] + 1
                # Add children to stack
                for i in range(2, N + 1):
                    if parent[i] == node:
                        stack.append(i)
    print('\n'.join(output))

if __name__ == '__main__':
    main()
