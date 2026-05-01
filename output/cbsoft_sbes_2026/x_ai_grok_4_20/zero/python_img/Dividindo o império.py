
import sys
sys.setrecursionlimit(10**6)

N = int(input())
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

subtree = [0] * (N+1)
min_diff = float('inf')

def dfs(node, parent):
    global min_diff
    subtree[node] = 1
    for child in graph[node]:
        if child != parent:
            dfs(child, node)
            subtree[node] += subtree[child]
            diff = abs(N - 2 * subtree[child])
            if diff < min_diff:
                min_diff = diff

dfs(1, -1)
print(min_diff)
