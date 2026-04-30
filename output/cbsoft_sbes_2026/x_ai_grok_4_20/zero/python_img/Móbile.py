
import sys
sys.setrecursionlimit(20000)

N = int(input())
children = [[] for _ in range(N+1)]
parent = [0] * (N+1)

for _ in range(N):
    i, j = map(int, input().split())
    children[j].append(i)
    parent[i] = j

def dfs(node):
    if not children[node]:
        return 1, True
    sizes = []
    balanced = True
    for child in children[node]:
        sz, bal = dfs(child)
        if not bal:
            balanced = False
        sizes.append(sz)
    if len(set(sizes)) > 1:
        balanced = False
    total = 1 + sum(sizes)
    return total, balanced

root = 0
while parent[root] != 0:
    root = parent[root]

_, is_balanced = dfs(root)
print("bem" if is_balanced else "mal")
