
import sys
sys.setrecursionlimit(200000)

N = int(input())
adj = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

subtree = [0] * (N+1)
ans = float('inf')

def dfs(node, parent):
    global ans
    subtree[node] = 1
    for child in adj[node]:
        if child != parent:
            dfs(child, node)
            subtree[node] += subtree[child]
            diff = abs(N - 2 * subtree[child])
            if diff < ans:
                ans = diff

dfs(1, -1)
print(ans)
