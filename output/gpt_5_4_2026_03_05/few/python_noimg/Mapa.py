import sys

data = list(map(int, sys.stdin.read().split()))
if not data:
    sys.exit()

n = data[0]
adj = [[] for _ in range(n + 1)]

idx = 1
for _ in range(n - 1):
    a = data[idx]
    b = data[idx + 1]
    c = data[idx + 2]
    idx += 3
    if c == 0:
        adj[a].append(b)
        adj[b].append(a)

visited = [False] * (n + 1)
total_without_white = 0

for start in range(1, n + 1):
    if not visited[start]:
        stack = [start]
        visited[start] = True
        size = 0
        while stack:
            u = stack.pop()
            size += 1
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    stack.append(v)
        total_without_white += size * (size - 1) // 2

total_pairs = n * (n - 1) // 2
print(total_pairs - total_without_white)