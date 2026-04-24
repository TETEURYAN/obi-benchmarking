import sys
from collections import deque

data = sys.stdin.read().split()
idx = 0
test_num = 1

while True:
    C = int(data[idx])
    E = int(data[idx + 1])
    L = int(data[idx + 2])
    P = int(data[idx + 3])
    idx += 4
    if C == 0 and E == 0 and L == 0 and P == 0:
        break
    adj = [[] for _ in range(C + 1)]
    for _ in range(E):
        X = int(data[idx])
        Y = int(data[idx + 1])
        idx += 2
        adj[X].append(Y)
        adj[Y].append(X)
    visited = [False] * (C + 1)
    dist = [-1] * (C + 1)
    q = deque()
    q.append(L)
    visited[L] = True
    dist[L] = 0
    while q:
        u = q.popleft()
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                dist[v] = dist[u] + 1
                if dist[v] <= P:
                    q.append(v)
    result = []
    for v in range(1, C + 1):
        if v != L and dist[v] != -1 and dist[v] <= P:
            result.append(v)
    result.sort()
    print(f"Teste {test_num}")
    if result:
        print(' '.join(map(str, result)))
    else:
        print()
    print()
    test_num += 1