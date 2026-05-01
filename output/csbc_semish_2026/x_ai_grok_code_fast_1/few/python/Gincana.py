import sys
from collections import deque

input_data = sys.stdin.read().split()
n = int(input_data[0])
m = int(input_data[1])
adj = [[] for _ in range(n + 1)]
idx = 2
for _ in range(m):
    u = int(input_data[idx])
    v = int(input_data[idx + 1])
    adj[u].append(v)
    adj[v].append(u)
    idx += 2
visited = [False] * (n + 1)
components = 0
for i in range(1, n + 1):
    if not visited[i]:
        components += 1
        q = deque([i])
        visited[i] = True
        while q:
            u = q.popleft()
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    q.append(v)
print(components)