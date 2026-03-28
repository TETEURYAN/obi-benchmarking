import sys

sys.setrecursionlimit(200000)

input_data = sys.stdin.read().split()
if not input_data:
    exit()

S = int(input_data[0])
T = int(input_data[1])
P = int(input_data[2])

A = [0] * (S + 1)
for i in range(1, S + 1):
    A[i] = int(input_data[2 + i])

adj = [[] for _ in range(S + 1)]
idx = 3 + S
for _ in range(T):
    u = int(input_data[idx])
    v = int(input_data[idx+1])
    idx += 2
    
    if A[u] > A[v]:
        adj[u].append(v)
    elif A[v] > A[u]:
        adj[v].append(u)

memo = [-1] * (S + 1)

def dfs(u):
    if memo[u] != -1:
        return memo[u]
    
    max_visits = 0
    for v in adj[u]:
        max_visits = max(max_visits, 1 + dfs(v))
        
    memo[u] = max_visits
    return max_visits

print(dfs(P))