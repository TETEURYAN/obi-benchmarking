import sys

input_data = sys.stdin.read().split()
idx = 0
N = int(input_data[idx])
idx += 1
adj = [[] for _ in range(N + 1)]
for _ in range(N):
    A = int(input_data[idx])
    B = int(input_data[idx + 1])
    adj[A].append(B)
    idx += 2

# First DFS to get finishing times
finishing_time = []
visited = [False] * (N + 1)
for i in range(1, N + 1):
    if not visited[i]:
        stack = [(i, 0)]
        while stack:
            node, idx_nei = stack[-1]
            if idx_nei == 0:
                visited[node] = True
            if idx_nei < len(adj[node]):
                nei = adj[node][idx_nei]
                stack[-1] = (node, idx_nei + 1)
                if not visited[nei]:
                    stack.append((nei, 0))
            else:
                stack.pop()
                finishing_time.append(node)

# Transpose graph
adj_t = [[] for _ in range(N + 1)]
for u in range(1, N + 1):
    for v in adj[u]:
        adj_t[v].append(u)

# Second DFS on transpose graph
visited = [False] * (N + 1)
count = 0
for node in reversed(finishing_time):
    if not visited[node]:
        count += 1
        stack = [node]
        visited[node] = True
        while stack:
            curr = stack.pop()
            for nei in adj_t[curr]:
                if not visited[nei]:
                    visited[nei] = True
                    stack.append(nei)

if count == 1:
    print('S')
else:
    print('N')