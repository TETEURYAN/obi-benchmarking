
import sys
from collections import deque

input = sys.stdin.read
data = input().split()

index = 0
X = int(data[index])
index += 1
Y = int(data[index])
index += 1
N = int(data[index])
index += 1
A = int(data[index])
index += 1

cities = []
for i in range(N):
    x = int(data[index])
    index += 1
    y = int(data[index])
    index += 1
    cities.append((x, y))

MAXD = A // 100

dist = [[float('inf')] * N for _ in range(N)]
for i in range(N):
    dist[i][i] = 0
    xi, yi = cities[i]
    for j in range(i + 1, N):
        xj, yj = cities[j]
        dx = abs(xi - xj)
        dy = abs(yi - yj)
        if dx == 0 or dy == 0:
            d = dx + dy
            if d <= MAXD:
                dist[i][j] = 1
                dist[j][i] = 1

graph = [[] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if dist[i][j] == 1:
            graph[i].append(j)

def bfs(start):
    queue = deque([start])
    visited = [False] * N
    visited[start] = True
    component = []
    while queue:
        u = queue.popleft()
        component.append(u)
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                queue.append(v)
    return component

components = []
visited = [False] * N
for i in range(N):
    if not visited[i]:
        comp = bfs(i)
        for u in comp:
            visited[u] = True
        components.append(comp)

if not components:
    print(0)
    sys.exit(0)

comp_id = [-1] * N
for cid, comp in enumerate(components):
    for u in comp:
        comp_id[u] = cid

C = len(components)
super_graph = [set() for _ in range(C)]
for i in range(N):
    for j in range(N):
        if dist[i][j] == float('inf'):
            ci = comp_id[i]
            cj = comp_id[j]
            if ci != cj:
                super_graph[ci].add(cj)
                super_graph[cj].add(ci)

start_comp = comp_id[0]
if C == 1:
    print(0)
    sys.exit(0)

queue = deque([start_comp])
dist_comp = [-1] * C
dist_comp[start_comp] = 0
while queue:
    u = queue.popleft()
    for v in super_graph[u]:
        if dist_comp[v] == -1:
            dist_comp[v] = dist_comp[u] + 1
            queue.append(v)

ans = 0
for d in dist_comp:
    if d > 0:
        ans = max(ans, d)

print(ans)
