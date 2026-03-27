import sys
from collections import deque

input_data = sys.stdin.read().split()
idx = 0
N = int(input_data[idx])
idx += 1
p = [0] * (N + 1)
for i in range(2, N + 1):
    p[i] = int(input_data[idx])
    idx += 1
Q = int(input_data[idx])
idx += 1
children = [[] for _ in range(N + 1)]
for i in range(2, N + 1):
    children[p[i]].append(i)
for _ in range(Q):
    typ = int(input_data[idx])
    idx += 1
    if typ == 1:
        vj = int(input_data[idx])
        kj = int(input_data[idx + 1])
        idx += 2
        u = vj
        for _ in range(kj):
            u = p[u]
        print(u)
    else:
        v = int(input_data[idx])
        idx += 1
        descendants = []
        visited = [False] * (N + 1)
        queue = deque()
        queue.append(v)
        visited[v] = True
        while queue:
            u = queue.popleft()
            for child in children[u]:
                if not visited[child]:
                    visited[child] = True
                    queue.append(child)
                    descendants.append(child)
        for u in descendants:
            p[u] = v
        children[v] = descendants