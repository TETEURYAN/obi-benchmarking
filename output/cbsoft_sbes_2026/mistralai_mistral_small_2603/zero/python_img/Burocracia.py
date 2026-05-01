
import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    it = iter(data)
    N = int(next(it))
    p = [0] * (N + 1)
    for i in range(2, N + 1):
        p[i] = int(next(it))
    
    Q = int(next(it))
    queries = []
    for _ in range(Q):
        t = int(next(it))
        if t == 1:
            v = int(next(it))
            k = int(next(it))
            queries.append((1, v, k))
        else:
            v = int(next(it))
            queries.append((2, v))
    
    parent = [0] * (N + 1)
    for i in range(1, N + 1):
        parent[i] = p[i]
    
    def find_kth_ancestor(v, k):
        current = v
        for _ in range(k):
            current = parent[current]
        return current
    
    output = []
    for query in queries:
        if query[0] == 1:
            v, k = query[1], query[2]
            res = find_kth_ancestor(v, k)
            output.append(str(res))
        else:
            v = query[1]
            stack = [v]
            while stack:
                node = stack.pop()
                if parent[node] != v:
                    parent[node] = v
                    for i in range(1, N + 1):
                        if parent[i] == node:
                            stack.append(i)
    
    print('\n'.join(output))

if __name__ == '__main__':
    main()
