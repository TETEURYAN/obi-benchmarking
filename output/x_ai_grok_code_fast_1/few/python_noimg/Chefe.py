import sys

input_data = sys.stdin.read().split()
idx = 0
N = int(input_data[idx])
idx += 1
M = int(input_data[idx])
idx += 1
I = int(input_data[idx])
idx += 1
age = [0] * (N + 1)
for i in range(1, N + 1):
    age[i] = int(input_data[idx])
    idx += 1
edges = []
for _ in range(M):
    X = int(input_data[idx])
    Y = int(input_data[idx + 1])
    edges.append([X, Y])
    idx += 2
for _ in range(I):
    typ = input_data[idx]
    idx += 1
    if typ == 'T':
        A = int(input_data[idx])
        B = int(input_data[idx + 1])
        idx += 2
        for e in edges:
            if e[0] == A:
                e[0] = B
            elif e[0] == B:
                e[0] = A
            if e[1] == A:
                e[1] = B
            elif e[1] == B:
                e[1] = A
    else:
        E = int(input_data[idx])
        idx += 1
        rev_adj = [[] for _ in range(N + 1)]
        for X, Y in edges:
            rev_adj[Y].append(X)
        visited = [False] * (N + 1)
        stack = [E]
        visited[E] = True
        min_age = float('inf')
        found = False
        while stack:
            u = stack.pop()
            for v in rev_adj[u]:
                if not visited[v]:
                    visited[v] = True
                    stack.append(v)
                    min_age = min(min_age, age[v])
                    found = True
        if found:
            print(min_age)
        else:
            print('*')