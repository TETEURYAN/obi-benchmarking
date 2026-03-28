import sys

input_data = sys.stdin.read().split()
idx = 0
N = int(input_data[idx])
idx += 1
M = int(input_data[idx])
idx += 1

adj = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    u = int(input_data[idx])
    v = int(input_data[idx + 1])
    adj[u].append(v)
    adj[v].append(u)
    idx += 2

colors = [0] * (N + 1)

from collections import deque

def get_path(P, Q):
    if P == Q:
        return [P]
    visited = [False] * (N + 1)
    parent = [-1] * (N + 1)
    q = deque([P])
    visited[P] = True
    found = False
    while q:
        u = q.popleft()
        if u == Q:
            found = True
            break
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                q.append(v)
    path = []
    current = Q
    while current != -1:
        path.append(current)
        current = parent[current]
    path.reverse()
    return path

for _ in range(M):
    P = int(input_data[idx])
    Q = int(input_data[idx + 1])
    C = int(input_data[idx + 2])
    idx += 3
    path = get_path(P, Q)
    for node in path:
        colors[node] = C

print(' '.join(map(str, colors[1:])))