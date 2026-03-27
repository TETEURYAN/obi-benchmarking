import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

idx = 0
N = int(input_data[idx])
M = int(input_data[idx + 1])
idx += 2

adj = [[] for _ in range(N + 1)]
for _ in range(M):
    u = int(input_data[idx])
    v = int(input_data[idx + 1])
    adj[u].append(v)
    adj[v].append(u)
    idx += 2

visited = [False] * (N + 1)
result = []

for i in range(1, N + 1):
    if not visited[i]:
        # DFS to find component
        stack = [i]
        visited[i] = True
        max_color = i
        while stack:
            node = stack.pop()
            max_color = max(max_color, node)
            for nei in adj[node]:
                if not visited[nei]:
                    visited[nei] = True
                    stack.append(nei)
        result.append(max_color)

result.sort()
print(len(result))
print(*result)