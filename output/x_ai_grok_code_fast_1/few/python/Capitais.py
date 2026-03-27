import sys
from collections import deque

input_data = sys.stdin.read().split()
idx = 0
n = int(input_data[idx])
idx += 1

adj = [[] for _ in range(n + 1)]
for i in range(n - 1):
    u = int(input_data[idx])
    v = int(input_data[idx + 1])
    adj[u].append(v)
    adj[v].append(u)
    idx += 2

leaves = [i for i in range(1, n + 1) if len(adj[i]) == 1]

def bfs(start):
    dist = [-1] * (n + 1)
    dist[start] = 0
    q = deque([start])
    farthest = start
    while q:
        u = q.popleft()
        for v in adj[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                if dist[v] > dist[farthest]:
                    farthest = v
                q.append(v)
    return farthest, dist[farthest]

if n == 2:
    print(1)
else:
    f1, _ = bfs(leaves[0])
    f2, diam = bfs(f1)
    print((diam + 1) // 2)