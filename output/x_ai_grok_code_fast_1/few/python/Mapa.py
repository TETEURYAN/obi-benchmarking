import sys

input_data = sys.stdin.read().split()

N = int(input_data[0])
adj = [[] for _ in range(N + 1)]
idx = 1
for _ in range(N - 1):
    A = int(input_data[idx])
    B = int(input_data[idx + 1])
    C = int(input_data[idx + 2])
    adj[A].append((B, C))
    adj[B].append((A, C))
    idx += 3

visited = [False] * (N + 1)

def dfs(node):
    stack = [node]
    visited[node] = True
    size = 1
    while stack:
        curr = stack.pop()
        for nei, col in adj[curr]:
            if not visited[nei] and col == 0:
                visited[nei] = True
                stack.append(nei)
                size += 1
    return size

total_pairs = N * (N - 1) // 2
blue_pairs = 0
for i in range(1, N + 1):
    if not visited[i]:
        s = dfs(i)
        blue_pairs += s * (s - 1) // 2

E = total_pairs - blue_pairs
print(E)