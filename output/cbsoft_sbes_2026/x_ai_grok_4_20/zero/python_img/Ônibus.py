
import sys
sys.setrecursionlimit(20000)

N, A, B = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    p, q = map(int, input().split())
    graph[p].append(q)
    graph[q].append(p)

parent = [-1] * (N+1)
depth = [0] * (N+1)

def dfs(node, par, dep):
    parent[node] = par
    depth[node] = dep
    for nei in graph[node]:
        if nei != par:
            dfs(nei, node, dep+1)

dfs(A, -1, 0)

ans = 0
cur = B
while cur != A:
    cur = parent[cur]
    ans += 1

print(ans)
