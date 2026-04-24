import sys
from collections import deque

data = sys.stdin.read().split()
idx = 0
test_case = 1

while True:
    N = int(data[idx])
    idx += 1
    if N == 0:
        break
    adj = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        x = int(data[idx])
        y = int(data[idx + 1])
        idx += 2
        adj[x].append(y)
        adj[y].append(x)
    if N == 1:
        center = [1]
    elif N == 2:
        center = [1, 2]
    else:
        degree = [0] * (N + 1)
        for i in range(1, N + 1):
            degree[i] = len(adj[i])
        leaves = deque()
        for i in range(1, N + 1):
            if degree[i] == 1:
                leaves.append(i)
        remaining = N
        while remaining > 2:
            new_leaves = deque()
            while leaves:
                leaf = leaves.popleft()
                remaining -= 1
                for nei in adj[leaf]:
                    degree[nei] -= 1
                    if degree[nei] == 1:
                        new_leaves.append(nei)
            leaves = new_leaves
        center = list(leaves)
    center.sort()
    print(f"Teste {test_case}")
    print(center[0])
    print()
    test_case += 1