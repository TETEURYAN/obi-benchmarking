
import sys
sys.setrecursionlimit(100000)

N = int(input())
adj = [[] for _ in range(N+1)]
for _ in range(N-1):
    x, y = map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)

diameter = 0
farthest = 1

def dfs(u, p, dist, depths):
    global diameter, farthest
    depths[u] = dist
    if dist > diameter:
        diameter = dist
        farthest = u
    for v in adj[u]:
        if v != p:
            dfs(v, u, dist+1, depths)

depths1 = [0]*(N+1)
dfs(1, -1, 0, depths1)
u = farthest
diameter = 0
depths2 = [0]*(N+1)
dfs(u, -1, 0, depths2)
v = farthest
diameter = 0
depths3 = [0]*(N+1)
dfs(v, -1, 0, depths3)

D = max(depths2)
max_len = D + 1
count = 0

for i in range(1, N+1):
    d2 = depths2[i]
    d3 = depths3[i]
    if d2 + d3 == D:
        count += 1

print(max_len)
print(count)
