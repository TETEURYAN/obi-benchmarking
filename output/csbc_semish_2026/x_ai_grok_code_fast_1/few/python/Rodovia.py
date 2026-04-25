import sys

input_data = sys.stdin.read().split()
if not input_data:
    print(-1)
    sys.exit()

N = int(input_data[0])
M = int(input_data[1])
adj = [set() for _ in range(N + 1)]
idx = 2
for _ in range(M):
    x = int(input_data[idx])
    y = int(input_data[idx + 1])
    adj[x].add(y)
    idx += 2

# Find the node with maximum out-degree
max_deg = 0
A = -1
for i in range(1, N + 1):
    deg = len(adj[i])
    if deg > max_deg:
        max_deg = deg
        A = i

if A == -1 or max_deg == 0:
    print(-1)
    sys.exit()

# Iterative DFS from A to find reachable nodes
reachable = set()
stack = [A]
visited = [False] * (N + 1)
visited[A] = True
while stack:
    u = stack.pop()
    reachable.add(u)
    for v in adj[u]:
        if not visited[v]:
            visited[v] = True
            stack.append(v)

# Check for a B that is reachable, not A, and no direct edge
for b in reachable:
    if b != A and b not in adj[A]:
        print(A, b)
        sys.exit()

print(-1)