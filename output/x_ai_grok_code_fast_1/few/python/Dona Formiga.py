import sys

input_data = sys.stdin.read().split()
idx = 0
S = int(input_data[idx])
idx += 1
T = int(input_data[idx])
idx += 1
P = int(input_data[idx])
idx += 1
A = [int(input_data[idx + i]) for i in range(S)]
idx += S
adj = [[] for _ in range(S + 1)]
for _ in range(T):
    I = int(input_data[idx])
    J = int(input_data[idx + 1])
    idx += 2
    if A[I - 1] > A[J - 1]:
        adj[I].append(J)
    if A[J - 1] > A[I - 1]:
        adj[J].append(I)

visited = [False] * (S + 1)
def dfs(node):
    visited[node] = True
    count = 1
    for nei in adj[node]:
        if not visited[nei]:
            count += dfs(nei)
    return count

reachable = dfs(P) - 1
print(reachable)