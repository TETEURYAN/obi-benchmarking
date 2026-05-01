
import sys
from collections import defaultdict, deque

input = sys.stdin.read
data = input().split()

index = 0
X = int(data[index]); index += 1
Y = int(data[index]); index += 1
N = int(data[index]); index += 1
A = int(data[index]); index += 1

cities = []
for i in range(N):
    x = int(data[index]); index += 1
    y = int(data[index]); index += 1
    cities.append((x, y))

MAX_DIST = A // 100

def can_reach(i, j):
    dx = abs(cities[i][0] - cities[j][0])
    dy = abs(cities[i][1] - cities[j][1])
    if dx > 0 and dy > 0:
        return False
    return max(dx, dy) <= MAX_DIST

graph = [[] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if i != j and can_reach(i, j):
            graph[i].append(j)

def bfs(start):
    dist = [-1] * N
    dist[start] = 0
    q = deque([start])
    while q:
        u = q.popleft()
        for v in graph[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                q.append(v)
    return dist

components = []
visited = [False] * N
for i in range(N):
    if not visited[i]:
        comp = []
        dist = bfs(i)
        for j in range(N):
            if dist[j] != -1:
                visited[j] = True
                comp.append(j)
        components.append(comp)

if not components:
    print(0)
    sys.exit(0)

start_comp = None
for idx, comp in enumerate(components):
    if 0 in comp:
        start_comp = idx
        break

if start_comp is None:
    components[0].append(0)
    start_comp = 0

K = len(components)
if K == 1:
    print(0)
    sys.exit(0)

adj_comp = [set() for _ in range(K)]
for i in range(K):
    for u in components[i]:
        for v_idx in graph[u]:
            for j in range(K):
                if j != i and v_idx in components[j]:
                    adj_comp[i].add(j)
                    break

dist_comp = [-1] * K
dist_comp[start_comp] = 0
q = deque([start_comp])
while q:
    u = q.popleft()
    for v in adj_comp[u]:
        if dist_comp[v] == -1:
            dist_comp[v] = dist_comp[u] + 1
            q.append(v)

max_d = 0
for d in dist_comp:
    if d > max_d:
        max_d = d

print(max_d)
